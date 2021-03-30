#include <iostream>
using namespace std;

enum RBNodeColor{
    BLACK = 1,
    RED = 0
};

struct Node {
    int value;
    RBNodeColor color;
    Node *left_tree, *right_tree, *parent;

    Node(): value(0), color(RED), left_tree(nullptr), right_tree(nullptr), parent(nullptr)
    {
    }

    Node* GrandParent()
    {
        if (parent == nullptr) {
            return nullptr;
        }
        return parent->parent;
    }

    Node* Uncle()
    {
        if (GrandParent() == nullptr) {
            return nullptr;
        }
        if (parent == GrandParent()->right_tree)
            return GrandParent()->left_tree;
        else
            return GrandParent()->right_tree;
    }

    Node* sibling()
    {
        if (parent->left_tree == this)
            return parent->right_tree;
        else
            return parent->left_tree;
    }
};

class RBTree {
private:
    void RotateRight(Node* p)
    {
        Node* gp = p->GrandParent();
        Node* parent = p->parent;
        Node* y = p->right_tree;

        parent->left_tree = y;

        if (y != NIL)
            y->parent = parent;

        p->right_tree = parent;
        parent->parent = p;

        if (root == parent)
            root = p;
        p->parent = gp;

        if (gp != nullptr) {
            if (gp->left_tree == parent)
                gp->left_tree = p;
            else
                gp->right_tree = p;
        }
    }

    void RotateLeft(Node* p)
    {
        if (p->parent == nullptr) {
            root = p;
            return;
        }

        Node* grand = p->GrandParent();
        Node* parent = p->parent;
        Node* y = p->left_tree;

        parent->right_tree = y;

        if (y != NIL)
            y->parent = parent;
        p->left_tree = parent;
        parent->parent = p;

        if (root == parent)
            root = p;
        p->parent = grand;

        if (grand != nullptr) {
            if (grand->left_tree == parent)
                grand->left_tree = p;
            else
                grand->right_tree = p;
        }
    }

    void InOrder(Node* p)
    {
        if (p == NIL)
            return;

        if (p->left_tree)
            InOrder(p->left_tree);

        cout << p->value << " ";

        if (p->right_tree)
            InOrder(p->right_tree);
    }

    string OutputColor(bool color)
    {
        return color ? "BLACK" : "RED";
    }

    Node* GetSmallestChild(Node* p)
    {
        if (p->left_tree == NIL)
            return p;
        return GetSmallestChild(p->left_tree);
    }

    bool DeleteChild(Node* p, int data)
    {
        if (p->value > data) {
            if (p->left_tree == NIL) {
                return false;
            }
            return DeleteChild(p->left_tree, data);
        } else if (p->value < data) {
            if (p->right_tree == NIL) {
                return false;
            }
            return DeleteChild(p->right_tree, data);
        } else if (p->value == data) {
            if (p->right_tree == NIL) {
                DeleteOneChild(p);
                return true;
            }
            Node* smallest = GetSmallestChild(p->right_tree);
            swap(p->value, smallest->value);
            DeleteOneChild(smallest);
            return true;
        } else {
            return false;
        }
    }

    void DeleteOneChild(Node* p)
    {
        Node* child = p->left_tree == NIL ? p->right_tree : p->left_tree;
        if (p->parent == nullptr && p->left_tree == NIL && p->right_tree == NIL) {
            p = nullptr;
            root = p;
            return;
        }

        if (p->parent == nullptr) {
            delete p;
            child->parent = nullptr;
            root = child;
            root->color = BLACK;
            return;
        }

        if (p->parent->left_tree == p) {
            p->parent->left_tree = child;
        } else {
            p->parent->right_tree = child;
        }
        child->parent = p->parent;

        if (p->color == BLACK) {
            if (child->color == RED) {
                child->color = BLACK;
            } else
                DeleteCase(child);
        }

        delete p;
    }

    void DeleteCase(Node* p)
    {
        if (p->parent == nullptr) {
            p->color = BLACK;
            return;
        }
        if (p->sibling()->color == RED) {
            p->parent->color = RED;
            p->sibling()->color = BLACK;
            if (p == p->parent->left_tree)
                RotateLeft(p->parent);
            else
                RotateRight(p->parent);
        }
        if (p->parent->color == BLACK && p->sibling()->color == BLACK
            && p->sibling()->left_tree->color == BLACK && p->sibling()->right_tree->color == BLACK) {
            p->sibling()->color = RED;
            DeleteCase(p->parent);
        } else if (p->parent->color == RED && p->sibling()->color == BLACK
            && p->sibling()->left_tree->color == BLACK && p->sibling()->right_tree->color == BLACK) {
            p->sibling()->color = RED;
            p->parent->color = BLACK;
        } else {
            if (p->sibling()->color == BLACK) {
                if (p == p->parent->left_tree && p->sibling()->left_tree->color == RED
                    && p->sibling()->right_tree->color == BLACK) {
                    p->sibling()->color = RED;
                    p->sibling()->left_tree->color = BLACK;
                    RotateRight(p->sibling()->left_tree);
                } else if (p == p->parent->right_tree && p->sibling()->left_tree->color == BLACK
                    && p->sibling()->right_tree->color == RED) {
                    p->sibling()->color = RED;
                    p->sibling()->right_tree->color = BLACK;
                    RotateLeft(p->sibling()->right_tree);
                }
            }
            p->sibling()->color = p->parent->color;
            p->parent->color = BLACK;
            if (p == p->parent->left_tree) {
                p->sibling()->right_tree->color = BLACK;
                RotateLeft(p->sibling());
            } else {
                p->sibling()->left_tree->color = BLACK;
                RotateRight(p->sibling());
            }
        }
    }

    void Insert(Node* p, int data)
    {
        if (data <= p->value) {
            // 放在左边
            if (p->left_tree != NIL)
                Insert(p->left_tree, data);
            else {
                // 左边不存在，创建一个新的节点
                Node* tmp = new Node();
                tmp->value = data;
                tmp->left_tree = tmp->right_tree = NIL;
                tmp->parent = p;
                p->left_tree = tmp;
                // 开始旋转
                InsertCase(tmp);
            }
        } else {
            // 放在右边
            if (p->right_tree != NIL)
                Insert(p->right_tree, data);
            else {
                Node* tmp = new Node();
                tmp->value = data;
                tmp->left_tree = tmp->right_tree = NIL;
                tmp->parent = p;
                p->right_tree = tmp;
                InsertCase(tmp);
            }
        }
    }

/*
1 节点是红色或黑色
2 根是黑色
3 所有叶子都是黑色（叶子是NIL节点）
4 每个红色节点必须有两个黑色的子节点。（从每个叶子到根的所有路径上不能有两个连续的红色节点。）
5 从任一节点到其每个叶子的所有简单路径都包含相同数目的黑色节点。
*/

    void InsertCase(Node* p)
    {
        if (p->parent == nullptr) {
            root = p;
            p->color = BLACK;
            return;
        }
        if (p->parent->color == RED) {
            // 父节点是红色，需要处理
            if (p->Uncle()->color == RED) {
                // 叔叔也是红色
                p->parent->color = p->Uncle()->color = BLACK;
                p->GrandParent()->color = RED;
                InsertCase(p->GrandParent());
            } else {
                // 叔叔节点是黑色，分为四种情况
                if (p->parent->right_tree == p && p->GrandParent()->left_tree == p->parent) {
                    RotateLeft(p);
                    p->color = BLACK;
                    p->parent->color = RED;
                    RotateRight(p);
                } else if (p->parent->left_tree == p && p->GrandParent()->right_tree == p->parent) {
                    RotateRight(p);
                    p->color = BLACK;
                    p->parent->color = RED;
                    RotateLeft(p);
                } else if (p->parent->left_tree == p && p->GrandParent()->left_tree == p->parent) {
                    p->parent->color = BLACK;
                    p->GrandParent()->color = RED;
                    RotateRight(p->parent);
                } else if (p->parent->right_tree == p && p->GrandParent()->right_tree == p->parent) {
                    p->parent->color = BLACK;
                    p->GrandParent()->color = RED;
                    RotateLeft(p->parent);
                }
            }
        }
    }

    void DeleteTree(Node* p)
    {
        if (!p || p == NIL) {
            return;
        }
        DeleteTree(p->left_tree);
        DeleteTree(p->right_tree);
        delete p;
    }

public:
    RBTree()
    {
        NIL = new Node();
        NIL->color = BLACK;
        root = nullptr;
    }

    ~RBTree()
    {
        if (root)
            DeleteTree(root);
        delete NIL;
    }

    void InOrder()
    {
        if (root == nullptr)
            return;
        InOrder(root);
        cout << endl;
    }

    void Insert(int x)
    {
        if (root == nullptr) {
            root = new Node();
            root->color = BLACK;
            root->left_tree = root->right_tree = NIL;
            root->value = x;
        } else {
            Insert(root, x);
        }
    }

    bool DeleteValue(int data)
    {
        return DeleteChild(root, data);
    }

private:
    Node *root;
    Node *NIL;
};

int main()
{
    RBTree b;
    for (int i = 0; i < 10; i++) {
        b.Insert(rand() % 100);
    }
    b.InOrder();
    return 0;
}
