#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

class RBTree {
private:
    enum Color {
        RED,
        BLACK
    };
    enum Direction {
        LEFT,
        RIGHT
    };

public:
    struct RBTreeNode {
        int k = 0;
        int v = 0;
        RBTreeNode* p = nullptr;
        RBTreeNode* left = nullptr;
        RBTreeNode* right = nullptr;
        Color color = RED;

        RBTreeNode(int k, int v, Color color)
            : k(k)
            , v(v)
            , color(color)
        {
            left = NIL;
            right = NIL;
            p = NIL;
        }

        bool isLeft(){
            return this == p->left;
        }

        bool isRight(){
            return this == p->right;
        }

        RBTreeNode * brother(){
            return isLeft()?p->right:p->left;
        }

        void replaceChild(RBTreeNode* n, RBTreeNode* new_node)
        {
            if (n == left) {
                left = new_node;
            } else {
                right = new_node;
            }
        }

        void addChild(RBTree * t, RBTreeNode * z){
            auto y = this;
            if (y == NIL) {
                t->root = z;
            } else if (z->k < y->k) {
                y->left = z;
            } else {
                y->right = z;
            }
        }

        static RBTreeNode* NIL;
    };

public:
    RBTree()
    {
        nil = RBTreeNode::NIL;
    }

    void leftRotate(RBTreeNode* x)
    {
        // n左移，n的右孩子r成为根节点，r的左孩子成为n的右孩子，其他不动
        // 看起来就像是n左移了
        auto y = x->right;
        x->right = y->left;
        if(y->left != nil){
            y->left->p = x;
        }
        y->p = x->p;

        if(x->p == nil){
            root = y;
        }else{
            x->p->replaceChild(x, y);
        }

        y->left = x;
        x->p = y;
    }
    void rightRotate(RBTreeNode* x)
    {
        // n右移，n的左孩子l成为根节点，l的右孩子成为n的左孩子，其他不动
        // 看起来就像是n右移了
        auto y = x->left;
        x->left = y->right;
        if(y->right != nil){
            y->right->p = x;
        }
        y->p = x->p;

        if(x->p == nil){
            root = y;
        }else{
            x->p->replaceChild(x, y);
        }

        y->right = x;
        x->p = y;
    }

    RBTreeNode* getInternal(RBTreeNode* n, int k)
    {
        if (!n) {
            return nullptr;
        }
        if (n->k == k) {
            return n;
        }
        if (k < n->k) {
            return getInternal(n->left, k);
        }
        return getInternal(n->right, k);
    }

    int get(int key)
    {
        // 普通的搜索
        auto v = getInternal(root, key);
        return v ? v->v : -1;
    }

    void insert(RBTreeNode* n, RBTreeNode* z)
    {
        auto y = nil;
        auto x = root;
        // 找到父节点
        while (x != nil) {
            y = x;
            if (z->k < x->k) {
                x = x->left;
            } else {
                x = x->right;
            }
        }

        z->p = y;
        y->addChild(this, z);
        insert_fixup(z);
        dump(y);
    }

    void dumpInternal(RBTreeNode * n, int d){
        if(!n)return;
        for(int i=0; i<d; i++)printf("--");
        printf("%d(%d %d)\n", n->v, n->k, n->v);
        dumpInternal(n->left, d+1);
        dumpInternal(n->right, d+1);
    }

    void dump(RBTreeNode * n){
        dumpInternal(n, 1);
    }

    /*
    1 父子节点之间不能出现两个连续的红节点
    2 任何一个节点向下遍历到其子孙的叶子节点，所经过的黑节点个数必须相等
    */
    void insert_fixup(RBTreeNode* z)
    {
        // 处理父节点是红色，父子同为红色冲突了
        while (z->p->color == RED) {
            // 父节点在左边
            if (z->p->isLeft()) {
                // 找到叔叔
                auto y = z->p->brother();
                // case 1
                if (y->color == RED) {
                    // 父亲和叔叔都是红色，把他们都变成黑色
                    z->p->color = BLACK;
                    y->color = BLACK;
                    // 把祖父变成红色
                    z->p->p->color = RED;
                    z = z->p->p;
                } else {
                    // 父亲是红色，叔叔是黑色
                    if (z->isRight()){
                        // z在右边就左旋，z指向父节点
                        z = z->p;
                        // 左旋父节点
                        leftRotate(z);
                    }
                    // 父亲设置为黑色
                    z->p->color = BLACK;
                    // 把祖父变成红色
                    z->p->p->color = RED;
                    // 右旋祖父节点
                    rightRotate(z->p->p);
                }
            }else{
                auto y = z->p->brother();
                // case 1
                if (y->color == RED) {
                    z->p->color = BLACK;
                    y->color = BLACK;
                    z->p->p->color = RED;
                    z = z->p->p;
                } else {
                    if (z->isLeft()){
                        z = z->p;
                        rightRotate(z);
                    }
                    
                    z->p->color = BLACK;
                    z->p->p->color = RED;
                    leftRotate(z->p->p);
                }
            }
        }
        root->color = BLACK;
    }

    void set(int k, int v)
    {
        if (!root) {
            printf("set root %d %d\n", k, v);
            root = new RBTreeNode(k, v, BLACK);
        }else{
            printf("insert %d %d\n", k, v);
            auto z = new RBTreeNode(k, v, RED);
            insert(root, z);
        }
    }

private:
    RBTreeNode* root = nullptr;
    RBTreeNode* nil = nullptr;
};

RBTree::RBTreeNode* RBTree::RBTreeNode::NIL = new RBTree::RBTreeNode(0, 0, RBTree::BLACK);

int main()
{
    RBTree t;
    int n = 40;
    for(int i=1; i<=n; i++){
        t.set(i, i);
    }
    
    for(int i=1; i<=n; i++){
        printf("get %d %d\n", i, t.get(i));
    }
    
    return 0;
}
