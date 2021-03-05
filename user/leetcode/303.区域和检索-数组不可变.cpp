/*
 * @lc app=leetcode.cn id=303 lang=cpp
 *
 * [303] 区域和检索 - 数组不可变
 */
#include <vector>
using namespace std;

// @lc code=start
class NumArray {
public:
    int f[10010];
    NumArray(vector<int>& nums) {
        // 让数组下标从1开始，便于处理偏移
        f[0] = 0;
        for(int i=0; i<nums.size(); i++){
            f[i+1] = f[i]+nums[i];
        }
    }
    
    int sumRange(int i, int j) {
        return f[j+1] - f[i];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(i,j);
 */
// @lc code=end

