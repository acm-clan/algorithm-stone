/*
 * @lc app=leetcode.cn id=451 lang=cpp
 *
 * [451] 根据字符出现频率排序
 */
#include <queue>
#include <map>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <iostream>
using namespace std;

// author dansen
// @lc code=start
class Solution {
public:
    struct Node{
        char c;
        int count;
    };
    string frequencySort(string s) {
        int t[128];
        memset(t, 0, sizeof(t));
        for(auto & c: s){
            t[c]++;
        }
        auto cmp = [](pair<int, int> & a, pair<int, int> & b){
            return a.second < b.second;
        };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> q(cmp);
        // 注意这里不能使用i<sizeof(t)
        for(int i=0; i<128; i++){
            if(t[i] > 0){
                q.emplace(i, t[i]);
            }
        }
        string v;
        while(q.size()){
            auto top = q.top();
            v.append(top.second, (char)top.first);
            q.pop();
        }
        return v;
    }
};

// @lc code=end

