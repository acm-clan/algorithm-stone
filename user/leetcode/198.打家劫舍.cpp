/*
 * @lc app=leetcode.cn id=198 lang=cpp
 *
 * [198] 打家劫舍
 */

// @lc code=start
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n == 0){
            return 0;
        }
        if(n == 1){
            return nums[0];
        }
        int f[n+10];
        f[0] = nums[0];
        f[1] = nums[1];
        for(int i=2; i<n; i++){
            int m = 0;
            for(int j=0; j<i-1; j++){
                m = max(m, f[j]);
            }
            f[i] = m+nums[i];
        }
        return max(f[n-2], f[n-1]);
    }
};
// @lc code=end

