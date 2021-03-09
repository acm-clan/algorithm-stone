/*
 * @lc app=leetcode.cn id=935 lang=cpp
 *
 * [935] 骑士拨号器
 */

// @lc code=start
class Solution {
public:
    int knightDialer(int N) {
        int steps[N + 1][10];
        int mod = 1000000007;
        for(int i = 0; i < 10; i ++) {
            steps[1][i] = 1;
        }
        // 每一步都依赖前一步
        for(int i = 2; i <= N; i ++) {
            steps[i][0] = (steps[i - 1][4] + steps[i - 1][6]) % mod;
            steps[i][1] = (steps[i - 1][6] + steps[i - 1][8]) % mod;
            steps[i][2] = (steps[i - 1][7] + steps[i - 1][9]) % mod;
            steps[i][3] = (steps[i - 1][4] + steps[i - 1][8]) % mod;
            steps[i][4] = ((steps[i - 1][3] + steps[i - 1][9]) % mod + steps[i - 1][0]) % mod;
            steps[i][5] = 0;
            steps[i][6] = ((steps[i - 1][1] + steps[i - 1][7]) % mod + steps[i - 1][0]) % mod;
            steps[i][7] = (steps[i - 1][2] + steps[i - 1][6]) % mod;
            steps[i][8] = (steps[i - 1][1] + steps[i - 1][3]) % mod;
            steps[i][9] = (steps[i - 1][4] + steps[i - 1][2]) % mod;
        }
        int ans = 0;
        // 统计所有的第N步
        for(int i = 0; i < 10; i ++) {
            ans += steps[N][i];
            ans %= mod;
        }
        return ans;
    }
};
// @lc code=end

