/*
 * @lc app=leetcode.cn id=121 lang=cpp
 *
 * [121] 买卖股票的最佳时机
 */

// @lc code=start
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int f[n];
        f[0] = 0;

        // 记录一个当前的最小值
        int mi = prices[0];
        for(int i=1; i<n; i++){
            int d = prices[i]-mi;
            // 使用上一次的
            f[i] = f[i-1];
            if(d > 0){
                // 更新较大值
                f[i] = max(f[i-1], d);
                //printf("f[%d]=%d\n", i, f[i]);
            }
            mi = min(mi, prices[i]);
        }
        return f[n-1];
    }
};
// @lc code=end

