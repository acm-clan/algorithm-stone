/*
 * @lc app=leetcode.cn id=208 lang=cpp
 *
 * [208] 实现 Trie (前缀树)
 */

#include <vector>
#include <map>
#include <string>
using namespace std;

// @lc code=start
class Trie {
public:
    Trie* c [26];
    char v :1;
    /** Initialize your data structure here. */
    Trie() {
        memset(c, 0, sizeof(c));
        v = 0;
    }

    Trie* searchPrefix(string & prefix) {
        Trie* p = this;
        for(char &ch : prefix){
            char index = ch-'a';
            if(!p->c[index]){
                return 0;
            }
            p = p->c[index];
        }
        return p;
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        Trie* p = this;
        for(char &c:word){
            char index = c-'a';
            if(p->c[index] == 0){
                p->c[index] = new Trie();
            }
            p = p->c[index];
        }
        p->v = 1;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        Trie* v = searchPrefix(word);
        return v && v->v;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        return searchPrefix(prefix);
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
// @lc code=end

