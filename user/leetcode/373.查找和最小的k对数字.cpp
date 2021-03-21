/*
 * @lc app=leetcode.cn id=373 lang=cpp
 *
 * [373] 查找和最小的K对数字
 */

#include <queue>
#include <map>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <string>
using namespace std;

// author dansen
// @lc code=start
class Solution {
public:
    struct Node{
        int value;
        pair<int, int> p;
        Node(int v, pair<int, int> p):value(v), p(p){

        }
    };
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        if(nums1.empty() || nums2.empty()){
            return {};
        }
        auto cmp = [](Node & a, Node & b){
            return a.value > b.value;
        };
        priority_queue<Node, vector<Node>, decltype(cmp)> q(cmp);
        for(auto a: nums1){
            for(auto b: nums2){
                q.emplace(a+b, make_pair(a, b));
            }
        }
        vector<vector<int>> res;
        for(int i=0; i<k&&q.size(); i++){
            auto p = q.top();
            res.emplace_back(vector<int>({p.p.first, p.p.second}));
            q.pop();
        }
        return res;
    }
};
// @lc code=end

