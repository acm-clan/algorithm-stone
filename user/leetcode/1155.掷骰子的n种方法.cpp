/*
 * @lc app=leetcode.cn id=1155 lang=cpp
 *
 * [1155] 掷骰子的N种方法
 */

// @lc code=start
class Solution {
public:
    int numRollsToTarget(int d, int f, int target) {
        int mod = 1000000007;
        int dp[31][1001];
        memset(dp, 0, sizeof(dp));

        // 边界起点初始化
        // i表示为投掷骰子的个数，j为投掷得到的总点数
        int m = min(f, target);
        // 投一个骰子，只有一种情况
        for(int j = 1; j <= m; j++) {
            dp[1][j] = 1;
        }

        //进行顺推过程
        for(int i = 2; i <=d; i++) {
            for(int j = i; j <= i*f; j++) {
                for(int k = 1; k<=f && j>=k; k++) {
                    dp[i][j] += dp[i-1][j-k];
                    dp[i][j] %= mod;
                }
            }
        }

        return dp[d][target];
    }
};
// @lc code=end

