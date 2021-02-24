/*
 * @lc app=leetcode.cn id=64 lang=cpp
 *
 * [64] 最小路径和
 */

// @lc code=start
class Solution {
public:
    // f[i][j] = max(f[i-1][j], f[i][j-1])
    int minPathSum(vector<vector<int>>& g) {
        int m = g.size();
        int n = g[0].size();
        int f[m][n];
        f[0][0] = g[0][0];
        for(int i=1; i<m; i++){
            f[i][0] = f[i-1][0]+g[i][0];
        }
        for(int j=1; j<n; j++){
            f[0][j] = f[0][j-1]+g[0][j];
        }
        for(int i=1; i<m; i++){
            for(int j=1; j<n; j++){
                f[i][j] = min(f[i-1][j], f[i][j-1])+g[i][j];
            }
        }
        return f[m-1][n-1];
    }
};
// @lc code=end

