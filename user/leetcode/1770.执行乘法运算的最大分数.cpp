/*
 * @lc app=leetcode.cn id=1770 lang=cpp
 *
 * [1770] 执行乘法运算的最大分数
 */

// @lc code=start
class Solution {
public:
    int maximumScore(vector<int>& nums, vector<int>& mu) {
        int n = nums.size();
        int m = mu.size();
        int f[1010][1010];
        f[0][0] = 0;
        int res = INT_MIN;

        for(int k=1; k<=m; k++){
            for(int i=0; i<=k; i++){
                int j = k-i;
                f[i][j] = INT_MIN;
                if(i>0){
                    //左边取值的情况
                    int t = f[i-1][j] + nums[i-1]*mu[k-1];
                    f[i][j] = max(t, f[i][j]);
                }
                if(j>0){
                    //右边取值的情况
                    int t = f[i][j-1] + nums[n-j]*mu[k-1];
                    f[i][j] = max(t, f[i][j]);
                }
                if(k==m){
                    res = max(res, f[i][j]);
                }
            }
        }

        return res;
    }
};
// @lc code=end

