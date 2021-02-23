/*
 * @lc app=leetcode.cn id=1137 lang=cpp
 *
 * [1137] 第 N 个泰波那契数
 */

// @lc code=start
class Solution {
public:
    int tribonacci(int n) {
        int f[n+10];
        f[0] = 0;
        f[1] = 1;
        f[2] = 1;
        for(int i=3; i<=n; i++){
            f[i] = f[i-1]+f[i-2]+f[i-3];
        }
        return f[n];
    }
};
// @lc code=end

