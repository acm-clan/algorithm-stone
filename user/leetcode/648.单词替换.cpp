/*
 * @lc app=leetcode.cn id=648 lang=cpp
 *
 * [648] 单词替换
 */
#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

// @lc code=start
class Solution {
public:
    class Trie{
    private:
        Trie * c[26];
        bool end=false;
    public:
        Trie(){
            memset(c, 0, sizeof(c));
        }

        void insert(string v){
            auto p = this;
            for(auto c : v){
                int i = c - 'a';
                if(!p->c[i]){
                    p->c[i] = new Trie();
                }
                p = p->c[i];
            }
            p->end = true;
        }

        void print(Trie * t){
            if(!t)return;
            
            for(int i=0; i<26; i++){
                if(t->c[i]){
                    printf("%c ", i+'a');
                    print(t->c[i]);
                    printf("\n");
                }
            }
        }

        void get_short(Trie * t, string & word, int i, string & con, bool & find){
            if(i >= word.length()){
                return;
            }
            auto index = word[i]-'a';
            if(!t->c[index]){
                return;
            }
            if(t->c[index]->end){
                con += word[i];
                find = true;
                return;
            }else{
                con += word[i];
                get_short(t->c[index], word, i+1, con, find);
            }
        }

        string get(string word){
            string con;
            int i=0;
            bool find = false;
            get_short(this, word, i, con, find);
            if(!find){
                con = word;
            }
            //printf("get word %s %s\n", word.c_str(), con.c_str());
            return con;
        }
    };
    string replaceWords(vector<string>& dictionary, string sentence) {
        Trie node;
        for(auto v : dictionary){
            node.insert(v);
        }
        //node.print(&node);

        string ans;
        string w;
        for(char c : sentence){
            if(c == ' '){
                ans += node.get(w)+" ";
                w = "";
            }else{
                w += c;
            }
        }
        ans += node.get(w);
        return ans;
    }
};
// @lc code=end

