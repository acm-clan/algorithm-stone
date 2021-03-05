/*
 * @lc app=leetcode.cn id=304 lang=cpp
 *
 * [304] 二维区域和检索 - 矩阵不可变
 */

#include <vector>
using namespace std;

// @lc code=start
class NumMatrix {
public:
    // 注意不需要太大
    int f[1001][1001];
    NumMatrix(vector<vector<int>>& matrix) {
        // 还是从1开始做下标
        int m = matrix.size();
        int n = 0;
        if(m)n=matrix[0].size();

        for(int i=0; i<=m; i++)f[i][0] = 0;
        for(int j=0; j<=n; j++)f[0][j] = 0;

        for(int i=1; i<=m; i++){
            for(int j=1; j<=n; j++){
                f[i][j] = f[i-1][j] + f[i][j-1] + matrix[i-1][j-1] - f[i-1][j-1];
            }
        }
    }
    
    int sumRegion(int row1, int col1, int row2, int col2) {
        // 要特别注意+1，画个图
        return f[row2+1][col2+1] - f[row1][col2+1] - f[row2+1][col1] + f[row1][col1];
    }
};

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix* obj = new NumMatrix(matrix);
 * int param_1 = obj->sumRegion(row1,col1,row2,col2);
 */
// @lc code=end

