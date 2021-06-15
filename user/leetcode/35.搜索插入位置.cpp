/*
 * @lc app=leetcode.cn id=35 lang=cpp
 *
 * [35] 搜索插入位置
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
    int searchInsert2(vector<int>& nums, int t) {
        int n = nums.size();
        int l=0, r=n-1;

        // ans初始选择最大值，然后让ans一直左移
        int ans = n;

        while(l<=r){
            int mid = l+r>>1;
            if(t==nums[mid]){
                return mid;
            }else if(t < nums[mid]){
                // 左移
                ans = mid;
                r = mid - 1;
            }else {
                l = mid + 1;
            }
        }
        return l;
    }
    int searchInsert(vector<int>& nums, int t) {
        int n = nums.size();
        int l=0, r=n-1;

        // ans初始选择最小值，然后让ans一直右移
        int ans = 0;

        while(l<=r){
            int mid = l+r>>1;
            if(t==nums[mid]){
                return mid;
            }else if(t < nums[mid]){
                r = mid - 1;
            }else {
                // 右移
                ans = mid;
                l = mid + 1;
            }
        }
        return l;
    }
};

// @lc code=end

