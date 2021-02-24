/*
 * @lc app=leetcode.cn id=120 lang=cpp
 *
 * [120] 三角形最小路径和
 */
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int minimumTotal(vector<vector<int>>& t) {
        int m = t.size();
        if(m == 1){
            return t[0][0];
        }
        int f[m][m];
        memset(f, 0, sizeof(f));
        f[0][0] = t[0][0];
        int mi = INT_MAX;
        for(int i=1; i<m; i++){
            for(int j=0; j<=i; j++){
                // 边界单独处理
                if(j == i){
                    f[i][j] = f[i-1][j-1]+t[i][j];
                }else if(j==0){
                    f[i][j] = f[i-1][j]+t[i][j];
                }else{
                    f[i][j] = min(f[i-1][j-1], f[i-1][j])+t[i][j];
                }
                
                if(i == m-1){
                    mi = min(f[i][j], mi);
                }
            }
        }
        return mi;
    }
};
// @lc code=end

