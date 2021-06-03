/*
 * @lc app=leetcode.cn id=211 lang=cpp
 *
 * [211] 添加与搜索单词 - 数据结构设计
 */
#include <vector>
#include <map>
#include <string>
using namespace std;
// @lc code=start
class WordDictionary {
    class Trie {
public:
    Trie* c [28];
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
            if(ch == '.')index=26;
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
        for(char &ch:word){
            char index = ch-'a';
            if(ch == '.')index=26;
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
public:
    Trie t;
    /** Initialize your data structure here. */
    WordDictionary() {

    }
    
    void addWord(string word) {
        t.insert(word);
    }
    
    bool search(string word) {
        return t.search(word);
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
// @lc code=end

