/*
 * @lc app=leetcode.cn id=53 lang=cpp
 *
 * [53] 最大子序和
 */

// @lc code=start
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n = nums.size();
        int f[n];
        f[0] = nums[0];
        int m = f[0];
        for(int i=1; i<n; i++){
            f[i] = nums[i];
            if(f[i-1] > 0){
                f[i] = f[i-1] + nums[i];
            }
            m = max(f[i], m);
        }
        return m;
    }
};
// @lc code=end

