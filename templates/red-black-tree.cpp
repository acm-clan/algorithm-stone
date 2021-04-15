#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

#include <time.h>

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

        bool isLeft()
        {
            return this == p->left;
        }

        bool isRight()
        {
            return this == p->right;
        }

        RBTreeNode* brother()
        {
            return isLeft() ? p->right : p->left;
        }

        void replaceChild(RBTreeNode* n, RBTreeNode* new_node)
        {
            if (n == left) {
                left = new_node;
            } else {
                right = new_node;
            }
            new_node->p = this;
        }

        void addChild(RBTree* t, RBTreeNode* z)
        {
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
        root = nil;
    }

    void leftRotate(RBTreeNode* x)
    {
        // x左移，x的右孩子y成为根节点，y的左孩子成为x的右孩子，其他不动
        // 看起来就像是x左移了
        auto y = x->right;

        // 1 x的右节点变化
        x->right = y->left;

        // 更新left的父节点
        if (y->left != nil) {
            y->left->p = x;
        }

        // 2 根节点变化，更换根节点
        y->p = x->p;

        // 如果x是根节点，将root设置为y
        transplant(x, y);

        // 3 y的左孩子
        y->left = x;
        x->p = y;
    }

    void rightRotate(RBTreeNode* x)
    {
        // x右移，x的左孩子y成为根节点，y的右孩子成为x的左孩子，其他不动
        // 看起来就像是x右移了
        auto y = x->left;

        x->left = y->right;

        // 更新right的父节点
        if (y->right != nil) {
            y->right->p = x;
        }

        y->p = x->p;

        transplant(x, y);

        y->right = x;
        x->p = y;
    }

    RBTreeNode* getInternal(RBTreeNode* n, int k)
    {
        if (!n || n == nil) {
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
                    // case 2 3
                    // 父亲是红色，叔叔是黑色
                    if (z->isRight()) {
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
            } else {
                auto y = z->p->brother();
                // case 1
                if (y->color == RED) {
                    z->p->color = BLACK;
                    y->color = BLACK;
                    z->p->p->color = RED;
                    z = z->p->p;
                } else {
                    if (z->isLeft()) {
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
        if (root == nil) {
            root = new RBTreeNode(k, v, BLACK);
        } else {
            auto z = new RBTreeNode(k, v, RED);
            insert(root, z);
        }
    }

    void transplant(RBTreeNode* u, RBTreeNode* v)
    {
        if (u->p == nil) {
            root = v;
            root->p = nil;
        } else {
            u->p->replaceChild(u, v);
        }
    }

    void deleteFixUp(RBTreeNode* x)
    {
        while (x != root && x->color == BLACK) {
            if (x->isLeft()) {
                auto w = x->brother();
                if (w->color == RED) {
                    w->color = BLACK;
                    x->p->color = RED;
                    leftRotate(x->p);
                    w = x->p->right;
                }
                if (w->left->color == BLACK && w->right->color == BLACK) {
                    w->color = RED;
                    x = x->p;
                } else {
                    if (w->right->color == BLACK) {
                        // printf("delete left case 3\n");
                        w->left->color = BLACK;
                        w->color = RED;
                        rightRotate(w);
                        w = x->p->right;
                    }

                    w->color = x->p->color;
                    x->p->color = BLACK;
                    w->right->color = BLACK;
                    leftRotate(x->p);
                    x = root;
                }
            } else {
                auto w = x->p->left;
                if (w->color == RED) {
                    w->color = BLACK;
                    x->p->color = RED;
                    rightRotate(x->p);
                    w = x->p->left;
                }
                if (w->right->color == BLACK && w->left->color == BLACK) {
                    w->color = RED;
                    x = x->p;
                } else {
                    if (w->left->color == BLACK) {
                        w->right->color = BLACK;
                        w->color = RED;
                        leftRotate(w);
                        w = x->p->left;
                    }

                    w->color = x->p->color;
                    x->p->color = BLACK;
                    w->left->color = BLACK;
                    rightRotate(x->p);
                    x = root;
                }
            }
        }
        x->color = BLACK;
    }

    RBTreeNode* treeMaxmum(RBTreeNode* x)
    {
        auto p = x;
        while (p != nil) {
            p = p->right;
        }
        return p;
    }

    RBTreeNode* treeMinimum(RBTreeNode* x)
    {
        auto p = x;
        while (p->left != nil) {
            p = p->left;
        }
        return p;
    }

    void deleteInternal(RBTreeNode* z)
    {
        auto y = z;
        auto origin_color = y->color;
        RBTreeNode* x = nullptr;

        if (z->left == nil) {
            x = z->right;
            transplant(z, z->right);
        } else if (z->right == nil) {
            x = z->left;
            transplant(z, z->left);
        } else {
            y = treeMinimum(z->right);
            origin_color = y->color;
            x = y->right;
            if (y->p == z) {
                x->p = y;
            } else {
                transplant(y, y->right);
                y->right = z->right;
                y->right->p = y;
            }
            transplant(z, y);
            y->left = z->left;
            y->left->p = y;
            y->color = z->color;
        }
        if (origin_color == BLACK) {
            deleteFixUp(x);
        }
    }

    void remove(int k)
    {
        auto z = getInternal(root, k);
        if (z) {
            deleteInternal(z);
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
    int i, count = 1000000;
    int key;

    srand(time(NULL));
    for (i = 1; i <= count; ++i) {
        key = rand() % count;
        t.set(key, i);
    }

    for (i = 1; i <= count; ++i) {
        key = rand() % count;
        t.remove(key);
    }

    return 0;
}
