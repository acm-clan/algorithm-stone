/*
 * @lc app=leetcode.cn id=1289 lang=cpp
 *
 * [1289] 下降路径最小和  II
 */

#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& g) {
        int n=g.size();
        int f[n][n];
        
        for(int j=0; j<n; j++){
            f[0][j]=g[0][j];
        }
        
        for(int i=1; i<n; i++){
            for(int j=0; j<n; j++){
                f[i][j] = INT_MAX;
                // 算出每个位置的最小值值
                for(int k=0; k<n; k++){
                    if(k!=j){
                        f[i][j] = min(f[i-1][k]+g[i][j], f[i][j]);
                    }
                }
            }
        }

        int m = INT_MAX;
        for(int j=0; j<n; j++){
            m = min(m, f[n-1][j]);
        }
        return m;
    }
};
// @lc code=end

