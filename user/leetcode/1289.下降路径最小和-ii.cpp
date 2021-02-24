/*
 * @lc app=leetcode.cn id=1289 lang=cpp
 *
 * [1289] 下降路径最小和  II
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
                int l = j-1;
                int r = j+1;

                if(l<0 || r>=n){
                    f[i][j] = INT_MAX/2;
                }else{
                    f[i][j] = min(f[i-1][l], f[i-1][r])+g[i][j];
                }
                printf("f[%d][%d]=%d\n", i, j, f[i][j]);
            }
        }
        for(int j=0; j<n; j++){
            m = min(m, f[n-1][j]);
        }
        return m;
    }
};
// @lc code=end

