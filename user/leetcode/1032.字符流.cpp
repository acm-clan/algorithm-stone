/*
 * @lc app=leetcode.cn id=1032 lang=cpp
 *
 * [1032] 字符流
 */
#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

// @lc code=start
class StreamChecker {
    struct Node {
        bool isEnd = false;
        Node *next[26];
    } *root;

    int ar[2000], n = -1;
public:
    StreamChecker(vector<string>& words) {
        root = new Node();
        for (string& str : words) {
            Node* p = root;
            for (int i = str.length(); i > 0; --i) {
                int idx = str[i - 1] - 'a';
                if (p->next[idx] == nullptr) {
                    p->next[idx] = new Node();
                }
                p = p->next[idx];
            }
            p->isEnd = true;
        }
    }

    bool query(char letter) {
        ar[(++n) % 2000] = letter - 'a';
        int i = n, ma = max(i - 2000, -1);
        // 每次遇到一个字母就从根开始查找
        Node* p = root;
        for (; i > ma && p != nullptr; --i) {
            if (p->isEnd) return true;
            p = p->next[ar[i % 2000]];
        }
        return p != nullptr && p->isEnd;
    }
};

/**
 * Your StreamChecker object will be instantiated and called as such:
 * StreamChecker* obj = new StreamChecker(words);
 * bool param_1 = obj->query(letter);
 */
// @lc code=end

