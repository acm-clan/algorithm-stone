/*
 * @lc app=leetcode.cn id=704 lang=cpp
 *
 * [704] 二分查找
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
    int search(vector<int>& nums, int t) {
        int n = nums.size();
        int l=0, r = n-1;
        
        while(l<=r){
            int m = l+r>>1;
            if(t == nums[m]){
                return m;
            }else if (t < nums[m]){
                r = m-1;
            }else{
                l = m+1;
            }
        }
        return -1;
    }
};
// @lc code=end

