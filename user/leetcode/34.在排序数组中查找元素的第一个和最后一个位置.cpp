/*
 * @lc app=leetcode.cn id=34 lang=cpp
 *
 * [34] 在排序数组中查找元素的第一个和最后一个位置
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
    int lower(vector<int>& nums, int t){
        int l = 0, r = nums.size()-1;
        int ans = r;

        while(l<=r){
            int m = (l+r)/2;
            if(nums[m] >= t){
                ans = m;
                r = m-1;
            }else{
                // < t
                l = m+1;
            }
        }
        return nums[ans]==t?ans:-1;
    }
    int upper(vector<int>& nums, int t){
        int l = 0, r = nums.size()-1;
        int ans = 0;

        while(l<=r){
            int m = (l+r)/2;
            if(nums[m] > t){
                r = m-1;
            }else{
                // <= t
                ans = m;
                l = m+1;
            }
        }
        return nums[ans]==t?ans:-1;
    }
    vector<int> searchRange(vector<int>& nums, int t) {
        if(nums.empty()){
            return {-1, -1};
        }
        auto l = lower(nums, t), r = upper(nums, t);
        return {l, r};
    }
};
// @lc code=end

