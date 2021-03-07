/*
 * @lc app=leetcode.cn id=413 lang=cpp
 *
 * [413] 等差数列划分
 */

// 给你一串数字，返回这串数字中能够构成等差数列的子串的数目

// @lc code=start
class Solution {
public:
    int numberOfArithmeticSlices1(vector<int>& A) {
        int count = 0;
        int addend = 0;

        for (int i = 2; i < A.size(); i++)
            if (A[i - 1] - A[i] == A[i - 2] - A[i - 1])
                count += ++addend;
            else 
                addend = 0;

        return count;
    }

    int numberOfArithmeticSlices(vector<int>& A) {
        int n = A.size();
        if(n < 3) return 0;
        vector<int> dp(n); //dp[i]表示以i位置的数为结尾中形成等差数列的个数
        dp[0] = dp[1] = 0;
        int sum = 0;
        for(int i=2; i<n; i++) {
            if (A[i - 1] - A[i - 2] == A[i] - A[i - 1]) {
                dp[i] = dp[i - 1] + 1; //当前合法的等差数列长度>=3(以i为结尾等于3的等差数列个数为1,大于3的个数为dp[i - 1])
            } else {
                dp[i] = 0;
            }
            sum += dp[i]; //每个位置为结尾的都加上
        }
        return sum;
    }
};
// @lc code=end

