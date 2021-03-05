/*
 * @lc app=leetcode.cn id=264 lang=cpp
 *
 * [264] 丑数 II
 */

// 1, 2, 3, 4, 5, 6, 8, 9, 10, 12
// @lc code=start
class Solution {
public:
    int nthUglyNumber(int n) {
        if(n == 0) return 0;
        int dp[n];
        int index2 = 0;
        int index3 = 0;
        int index5 = 0;
        dp[0] = 1;
        for(int i = 1; i < n; i++) {
            // 选择最小值，斐波拉契数列的变种
            dp[i] = min(dp[index2] * 2, min(dp[index3] * 3,dp[index5] * 5));
            if(dp[i] == dp[index2] * 2) index2++;
            if(dp[i] == dp[index3] * 3) index3++;
            if(dp[i] == dp[index5] * 5) index5++;
        }
        return dp[n - 1];
    }
};
// @lc code=end

