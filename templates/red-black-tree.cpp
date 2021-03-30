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
        
        Node* gp = p->GrandParent();
        Node* fa = p->parent;
        Node* y = p->left_tree;

        fa->right_tree = y;

        if (y != NIL)
            y->parent = fa;
        p->left_tree = fa;
        fa->parent = p;

        if (root == fa)
            root = p;
        p->parent = gp;

        if (gp != nullptr) {
            if (gp->left_tree == fa)
                gp->left_tree = p;
            else
                gp->right_tree = p;
        }
    }

    void inorder(Node* p)
    {
        if (p == NIL)
            return;

        if (p->left_tree)
            inorder(p->left_tree);

        cout << p->value << " ";

        if (p->right_tree)
            inorder(p->right_tree);
    }

    string outputColor(bool color)
    {
        return color ? "BLACK" : "RED";
    }

    Node* getSmallestChild(Node* p)
    {
        if (p->left_tree == NIL)
            return p;
        return getSmallestChild(p->left_tree);
    }

    bool delete_child(Node* p, int data)
    {
        if (p->value > data) {
            if (p->left_tree == NIL) {
                return false;
            }
            return delete_child(p->left_tree, data);
        } else if (p->value < data) {
            if (p->right_tree == NIL) {
                return false;
            }
            return delete_child(p->right_tree, data);
        } else if (p->value == data) {
            if (p->right_tree == NIL) {
                delete_one_child(p);
                return true;
            }
            Node* smallest = getSmallestChild(p->right_tree);
            swap(p->value, smallest->value);
            delete_one_child(smallest);

            return true;
        } else {
            return false;
        }
    }

    void delete_one_child(Node* p)
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
                delete_case(child);
        }

        delete p;
    }

    void delete_case(Node* p)
    {
        if (p->parent == nullptr) {
            p->color = BLACK;
            return;
        }
        if (p->sibling()->color == RED) {
            p->parent->color = RED;
            p->sibling()->color = BLACK;
            if (p == p->parent->left_tree)
                //RotateLeft(p->sibling());
                RotateLeft(p->parent);
            else
                //RotateRight(p->sibling());
                RotateRight(p->parent);
        }
        if (p->parent->color == BLACK && p->sibling()->color == BLACK
            && p->sibling()->left_tree->color == BLACK && p->sibling()->right_tree->color == BLACK) {
            p->sibling()->color = RED;
            delete_case(p->parent);
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

    void insert(Node* p, int data)
    {
        if (p->value >= data) {
            if (p->left_tree != NIL)
                insert(p->left_tree, data);
            else {
                Node* tmp = new Node();
                tmp->value = data;
                tmp->left_tree = tmp->right_tree = NIL;
                tmp->parent = p;
                p->left_tree = tmp;
                insert_case(tmp);
            }
        } else {
            if (p->right_tree != NIL)
                insert(p->right_tree, data);
            else {
                Node* tmp = new Node();
                tmp->value = data;
                tmp->left_tree = tmp->right_tree = NIL;
                tmp->parent = p;
                p->right_tree = tmp;
                insert_case(tmp);
            }
        }
    }

    void insert_case(Node* p)
    {
        if (p->parent == nullptr) {
            root = p;
            p->color = BLACK;
            return;
        }
        if (p->parent->color == RED) {
            if (p->Uncle()->color == RED) {
                p->parent->color = p->Uncle()->color = BLACK;
                p->GrandParent()->color = RED;
                insert_case(p->GrandParent());
            } else {
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

    void inorder()
    {
        if (root == nullptr)
            return;
        inorder(root);
        cout << endl;
    }

    void insert(int x)
    {
        if (root == nullptr) {
            root = new Node();
            root->color = BLACK;
            root->left_tree = root->right_tree = NIL;
            root->value = x;
        } else {
            insert(root, x);
        }
    }

    bool delete_value(int data)
    {
        return delete_child(root, data);
    }

private:
    Node *root, *NIL;
};

int main()
{
    RBTree b;
    for (int i = 0; i < 10; i++) {
        b.insert(rand() % 100);
    }
    b.inorder();
    return 0;
}
