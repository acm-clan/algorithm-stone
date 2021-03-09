/*
 * @lc app=leetcode.cn id=576 lang=cpp
 *
 * [576] 出界的路径数
 */
#include <string>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int findPaths(int m, int n, int N, int i, int j) {
        long long f[N+1][m][n];
        memset(f, 0, sizeof(f));
        long long MOD=1000000007;
        
        // 走1步、2步...
        for(int k=1; k<=N; ++k){
            // 界面所有位置
            for(int x=0; x<m; ++x){
                 for(int y=0; y<n; ++y){
                    long long v1 = (x == 0) ? 1 : f[k-1][x-1][y];
                    long long v2 = (y == 0) ? 1 : f[k-1][x][y-1];
                    long long v3 = (x == m-1) ? 1 : f[k-1][x+1][y];
                    long long v4 = (y == n-1) ? 1 : f[k-1][x][y+1];
                    
                    f[k][x][y]=(v1+v2+v3+v4)%MOD;
                }
            }
        }
        
        return f[N][i][j];
    }
};
// @lc code=end

