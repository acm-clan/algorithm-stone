/*
 * @lc app=leetcode.cn id=349 lang=cpp
 *
 * [349] 两个数组的交集
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
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        set<int> s(nums1.begin(), nums1.end());
        set<int> ans;
        
        for(int j=0; j<nums2.size(); j++){
            if(s.find(nums2[j]) != s.end()){
                ans.insert(nums2[j]);
            }
        }
           
        return std::vector<int>(ans.begin(), ans.end());
    }
};
// @lc code=end

