/*
 * @lc app=leetcode.cn id=790 lang=cpp
 * 
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
        f[1][1] = 2;
        long long m = 1e9+7;
        for(int i=2; i<=N; i++){
            // f[i - 1][0]是竖着放一块
            // f[i - 2][0]只可能是2块横着放
            // f[i - 1][1]只可能固定一种结果
            f[i][0] = (f[i - 1][0] + f[i - 2][0] + f[i - 2][1]) % m;

            //f[i][1]表示有一个脚在i+1列，f[i - 1][0]上下放一个横板,f[i - 1][1]放一个横板
            f[i][1] = (f[i - 1][0]*2 + f[i - 1][1]) % m;
        }
        return f[N][0];
    }
};
// @lc code=end

