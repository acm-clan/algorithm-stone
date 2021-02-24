/*
 * @lc app=leetcode.cn id=63 lang=cpp
 *
 * [63] 不同路径 II
 */

// @lc code=start
class Solution {
public:
    int uniquePathsWithObstacles(vector<vector<int>>& g) {
        int m = g.size();
        int n = g[0].size();
        int f[m][n];

        f[0][0] = g[0][0]?0:1;

        for(int i=1; i<m; i++){
            f[i][0] = g[i][0]?0:f[i-1][0];
        }
        for(int j=1; j<n; j++){
            f[0][j] = g[0][j]?0:f[0][j-1];
        }
        for(int i=1; i<m; i++){
            for(int j=1; j<n; j++){
                if(g[i][j]){
                    f[i][j] = 0;
                }else{
                    f[i][j] = f[i-1][j] + f[i][j-1];
                }
            }
        }

        return f[m-1][n-1];
    }
};
// @lc code=end

