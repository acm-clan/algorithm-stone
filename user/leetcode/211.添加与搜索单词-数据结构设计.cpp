/*
 * @lc app=leetcode.cn id=211 lang=cpp
 *
 * [211] 添加与搜索单词 - 数据结构设计
 */
#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <string.h>
using namespace std;

// @lc code=start
struct Node {
    bool isword;
    Node* children[26];
    Node() {
        isword = false;
        for (auto& child : children)
            child = nullptr;
    }
};


class WordDictionary {
private:
    Node* root;
public:
    /** Initialize your data structure here. */
    WordDictionary() {
        root = new Node();
    }

    void addWord(string word) {
        Node* p = root;
        for (char& ch : word) {
            if (!p->children[ch - 'a'])
                p->children[ch - 'a'] = new Node();
            p = p->children[ch - 'a'];
        }
        p->isword = true;
    }

    bool search(string word) {
        return _search(word, root, 0);
    }

    bool _search(string& word, Node* p, int i) {
        if (!p) return false;

        if (i == word.size()) return p->isword;

        if (word[i] == '.') {
            for (int j = 0; j < 26; ++j) {
                if (_search(word, p->children[j], i+1))
                    return true;
            }
            return false;
        }
        return _search(word, p->children[word[i] - 'a'], i+1);
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
// @lc code=end
