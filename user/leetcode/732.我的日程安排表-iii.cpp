/*
 * @lc app=leetcode.cn id=732 lang=cpp
 *
 * [732] 我的日程安排表 III
 */

// @lc code=start
struct Node{
public:
    int start, end;
    int maxTime = 0;
    int delatTime = 0;
    Node *left;
    Node *right;
    Node(int _start, int _end) : start(_start), end(_end), left(NULL), right(NULL) {
    }
};

class MyCalendarThree {
public:
    Node* root;
    MyCalendarThree() {
        root = new Node(0, 1e9);
    }

    int book(int start, int end) {
        return insert(start, end, root);
    }

    int insert(int s, int e, Node *node) {
        int mid = (node->start + node->end) / 2;
        if (node->start >= s && node->end <= e) {
            node->delatTime++;
            node->maxTime++;
        } else if (node->end > s && node->start < e) {
            if (!node->left) node->left = new Node(node->start, mid);
            if (!node->right) node->right = new Node(mid, node->end);
            node->left->maxTime += node->delatTime;
            node->left->delatTime += node->delatTime;
            node->right->maxTime += node->delatTime;
            node->right->delatTime += node->delatTime;
            node->delatTime = 0;
            node->maxTime = max(node->maxTime, max(insert(s, e, node->left), insert(s, e, node->right)));
        }
        return node->maxTime;
    }
};

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree* obj = new MyCalendarThree();
 * int param_1 = obj->book(start,end);
 */
// @lc code=end

