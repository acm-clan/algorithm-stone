/*
 * @lc app=leetcode.cn id=118 lang=cpp
 *
 * [118] 杨辉三角
 */
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<vector<int>> generate(int n) {
        vector<vector<int>> f(n,  vector<int>(0, 0));
        f[0] = {1};

        for(int i=1; i<n; i++){
            for(int j=0; j<=i; j++){
                if(j==0){
                    f[i].push_back(f[i-1][j]);
                }else if(j==i){
                    f[i].push_back(f[i-1][j-1]);
                }
                else{
                    f[i].push_back(f[i-1][j-1]+f[i-1][j]);
                }
            }
        }
        return f;
    }
};
// @lc code=end

