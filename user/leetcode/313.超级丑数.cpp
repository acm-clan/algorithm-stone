/*
 * @lc app=leetcode.cn id=313 lang=cpp
 *
 * [313] 超级丑数
 */

// @lc code=start
class Solution {
public:
    int nthSuperUglyNumber(int n, vector<int>& primes) {
        int len = primes.size();
        int dp[n];
        memset(dp, 0, sizeof(dp));
        dp[0] = 1;
        int index[len];
        memset(index, 0, sizeof(index));
        for (int i = 1; i < n; i++) {
            int min = INT_MAX;
            // 取得最小值
            for (int j = 0; j < len; j++) {
                if (min > primes[j] * dp[index[j]]) {
                    min = primes[j] * dp[index[j]];
                }
            }
            dp[i] = min;
            // 增加index
            for (int j = 0; j < len; j++) {
                if (min == primes[j] * dp[index[j]]) {
                    index[j]++;
                }
            }

        }
        return dp[n - 1];
    }

    
};
// @lc code=end

