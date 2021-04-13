#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;


class RBTree
{
private:
    enum Color{
        RED,
        BLACK
    };
    enum Direction{
        LEFT,
        RIGHT
    };
    struct Node{
        int k = 0;
        int v = 0;
        Node * parent = nullptr;
        Node * left = NIL;
        Node * right = NIL;
        Color color = RED;
        Node(int k, int v, Color color):k(k), v(v), color(color){

        }
        void replaceChild(Node * n, Node * new_node){
            if(n == left){
                left = new_node;
            }else{
                right = new_node;
            }
        }
        static Node * NIL;
    };
    
public:
    RBTree(){
        Node::NIL = new Node(0, 0, BLACK);
    }
    
    void rotateLeft(Node * n){
        // n左移，n的右孩子r成为根节点，r的左孩子成为n的右孩子，其他不动
        // 看起来就像是n左移了
        auto r = n->right;
        n->parent->replaceChild(n, r);
        n->right = r->left;
        r->left = n;
    }
    void rotateRight(Node * n){
        // n右移，n的左孩子l成为根节点，l的右孩子成为n的左孩子，其他不动
        // 看起来就像是n右移了
        auto l = n->left;
        n->parent->replaceChild(n, l);
        n->left = l->right;
        l->right = n;
    }

    Node * getInternal(Node * n, int k){
        if(!n){
            return nullptr;
        }
        if(n->k == k){
            return n;
        }
        if(k < n->k){
            return getInternal(n->left, k);
        }
        return getInternal(n->right, k);
    }

    int get(int key){
        // 普通的搜索
        auto v = getInternal(root, key);
        return v?v->v:-1;
    }

    void insert(Node * n, int k, int v){
        
    }

    void set(int k, int v){
        if(!root){
            root = new Node(k, v, BLACK);
        }
        insert(root, k, v);
    }
private:
    Node * root = nullptr;
};


int main()
{
    RBTree t;
    return 0;
}
