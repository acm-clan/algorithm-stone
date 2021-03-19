/*
 * @lc app=leetcode.cn id=451 lang=cpp
 *
 * [451] 根据字符出现频率排序
 */
#include <queue>
#include <map>
#include <string>
using namespace std;


// @lc code=start
class Solution {
public:
    struct Node{
        char c;
        int count;
    };
    string frequencySort(string s) {
        char t[128];
        memset(t, 0, sizeof(t));
        for(auto & c: s){
            t[c]++;
        }
        auto cmp = [](pair<int, int> & a, pair<int, int> & b){
            return a.second < b.second;
        };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> q(cmp);
        for(int i=0; i<128; i++){
            if(t[i] > 0){
                q.emplace(i, t[i]);
            }
        }
        string v;
        while(q.size()){
            auto top = q.top();
            for(int i=0; i<top.second; i++){
                v += (char)top.first;
            }
            
            q.pop();
        }
        return v;
    }
};
// @lc code=end

