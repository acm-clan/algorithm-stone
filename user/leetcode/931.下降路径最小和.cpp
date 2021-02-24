/*
 * @lc app=leetcode.cn id=931 lang=cpp
 *
 * [931] 下降路径最小和
 */

// @lc code=start
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& g) {
        int n=g.size();
        int f[n][n];
        int m = INT_MAX;
        for(int j=0; j<n; j++){
            f[0][j]=g[0][j];
        }
        
        for(int i=1; i<n; i++){
            for(int j=0; j<n; j++){
                int l = (j-1) < 0?0:(j-1);
                int c = j;
                int r = (j+1) >= n?(n-1):(j+1);
                int k = g[i][j];
                f[i][j] = min(min(f[i-1][l],f[i-1][c]), f[i-1][r])+k;
                //printf("f[%d][%d]=%d\n", i, j, f[i][j]);
            }
        }
        for(int j=0; j<n; j++){
            m = min(m, f[n-1][j]);
        }
        return m;
    }
};
// @lc code=end

