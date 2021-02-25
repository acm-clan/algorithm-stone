/*
 * @lc app=leetcode.cn id=1301 lang=cpp
 * E 1 1
 * X X X
 * 1 1 S
 * 
 * ["E11","XXX","11S"]
 * [1301] 最大得分的路径数目
 */

#include <vector>
#include <string>
#include <algorithm>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> pathsWithMaxScore(vector<string>& board) {
        int m = board.size();
        int n = board[0].length();
        int f[m][n];
        int d[m][n];
        memset(f, 0, sizeof(f));
        memset(d, 0, sizeof(d));
        f[m-1][n-1] = 0;
        // 右侧
        for(int i=m-2; i>=0; i--){
            int j = n-1;
            if(board[i][j] == 'X'){
                f[i][j] = 0;
                d[i][j] = 0;
            }else{
                f[i][j] = f[i+1][j] ? (f[i+1][j]+board[i][j]-'0') : 0;
                d[i][j] = 1;
            }
            printf("d[%d][%d]=%d #", i, j, d[i][j]);
        }
        // 底下
        for(int j=n-2; j>=0; j--){
            int i = m-1;
            if(board[i][j] == 'X'){
                f[i][j] = 0;
                d[i][j] = 0;
            }else{
                f[i][j] = f[i][j+1]?(f[i][j+1]+board[i][j]-'0'):0;
                d[i][j] = 1;
            }
            printf("d[%d][%d]=%d #", i, j, d[i][j]);
        }
        for(int i=m-2; i>=0; i--){
            for(int j=n-2; j>=0; j--){
                if(board[i][j] == 'X'){
                    f[i][j] = 0;
                }else if(board[i][j] == 'E'){
                    f[i][j] = max(f[i+1][j], f[i][j+1]);

                    if(f[i][j] == f[i+1][j]){
                        d[i][j] += d[i+1][j];
                    }
                    if(f[i][j] == f[i][j+1]){
                        d[i][j] += d[i][j+1];
                    }
                }else{
                    int p = board[i][j]-'0';
                    int m = max(f[i+1][j+1],max(f[i+1][j], f[i][j+1]));
                    f[i][j] = m?(m+p):0;
                    if(f[i][j] == f[i+1][j]+p){
                        d[i][j] += d[i+1][j];
                    }
                    if(f[i][j] == f[i][j+1]+p){
                        d[i][j] += d[i][j+1];
                    }
                    if(f[i][j] == f[i+1][j+1]+p){
                        d[i][j] += d[i+1][j+1];
                    }
                }
                printf("f[%d][%d]=%d ", i, j, f[i][j]);
            }
        }
        return {f[0][0], d[0][0]};
    }
};
// @lc code=end

