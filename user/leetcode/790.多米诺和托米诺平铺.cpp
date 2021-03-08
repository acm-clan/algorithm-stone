/*
 * @lc app=leetcode.cn id=790 lang=cpp
 * class Solution:
    def numTilings(self, N):
        dp = [[0] * 2 for _ in range(N + 1)]
        dp[0][0] = 1
        dp[1][0] = 1
        for i in range(2, N + 1):
            dp[i][0] = (dp[i - 1][0] + dp[i - 2][0] + 2 * dp[i - 1][1]) % (10 ** 9 + 7)
            dp[i][1] = (dp[i - 2][0] + dp[i - 1][1]) % (10 ** 9 + 7)
        return dp[-1][0]

 * [790] 多米诺和托米诺平铺
 */

// @lc code=start
class Solution {
public:
    int numTilings(int N) {
        long long f[N+1][2];
        memset(f, 0, sizeof(f));
        f[0][0] = 1;
        f[1][0] = 1;
        long long m = 1e9+7;
        for(int i=2; i<=N; i++){
            f[i][0] = (f[i - 1][0] + f[i - 2][0] + 2 * f[i - 1][1]) % m;
            f[i][1] = (f[i - 2][0] + f[i - 1][1]) % m;
        }
        return f[N][0];
    }
};
// @lc code=end

