/*
 * @lc app=leetcode.cn id=746 lang=cpp
 *
 * [746] 使用最小花费爬楼梯
 */

// @lc code=start
class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        int f[n];
        f[0] = cost[0];
        f[1] = cost[1];
        for(int i=2; i<n; i++){
            // 两者中取得较小值
            f[i] = min(f[i-1]+cost[i], f[i-2]+cost[i]);
        }
        // 注意可以直接跳过最后一个元素
        return min(f[n-1], f[n-2]);
    }
};
// @lc code=end

