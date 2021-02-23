/*
 * @lc app=leetcode.cn id=213 lang=cpp
 *
 * [213] 打家劫舍 II
 */

// @lc code=start
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n == 0)return 0;
        if(n == 1)return nums[0];
        if(n == 2)return max(nums[0], nums[1]);
        int f[n+10];
        f[0] = nums[0];
        f[1] = nums[1];
        // 不让开头和末尾在一起
        for(int i=2; i<n-1; i++){
            int m = 0;
            for(int j=0; j<i-1; j++){
                m = max(m, f[j]);
            }
            f[i] = m + nums[i];
        }
        int r1 = max(f[n-2], f[n-3]);

        // 
        f[2] = nums[2];
        for(int i=3; i<n; i++){
            int m = 0;
            for(int j=1; j<i-1; j++){
                m = max(m, f[j]);
            }
            f[i] = m + nums[i];
        }
        int r2 = max(f[n-1], f[n-2]);
        return max(r1, r2);
    }
};
// @lc code=end

