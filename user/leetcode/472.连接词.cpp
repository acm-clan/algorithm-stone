/*
 * @lc app=leetcode.cn id=472 lang=cpp
 *
 * [472] 连接词
 */

// @lc code=start
class Solution {
public:
    int son[100000][26];
    int cnt[100000];
    int idx = 0;

    void insert(string s){
        int p = 0;
        for(int i = 0; i < s.size(); i++){
            int u = s[i] - 'a';
            if(!son[p][u]) son[p][u] = ++idx;
            p = son[p][u];
        }
        cnt[p]++;
    }

    bool query(string s){
        int n = s.size(), p = 0;
        if(n == 0) return true;
        for(int i = 0; i < n; i++){
            int u = s[i] - 'a';
            if(!son[p][u]) return false;
            
            if(cnt[son[p][u]] > 0){
                if(query(s.substr(i + 1, n))) return true;
            }
            p = son[p][u];
        }
        return false;
    }

    vector<string> findAllConcatenatedWordsInADict(vector<string>& words) {
        int n = words.size();
        vector<string> ans;
        sort(words.begin(), words.end(), [](string& a, string& b){
            return a.size() < b.size();
        });
        for(auto word : words){
            if(word.size() == 0) continue;
            if(query(word)){
                ans.push_back(word);
            }else{
                insert(word);
            }
        }
        return ans;
    }
};
// @lc code=end

