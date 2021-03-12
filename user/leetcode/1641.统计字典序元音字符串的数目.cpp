/*
 * @lc app=leetcode.cn id=1641 lang=cpp
 *
 * [1641] 统计字典序元音字符串的数目
 */

// @lc code=start
class Solution
{
public:
    int countVowelStrings(int n)
    {
        if (n == 0)
            return 0;
        if (n == 1)
            return 5;
        int ans[n + 1][5];
        ans[1][0] = 1;
        ans[1][1] = 2;
        ans[1][2] = 3;
        ans[1][3] = 4;
        ans[1][4] = 5;
        for (int i = 2; i <= n; i++)
        {
            for (int j = 0; j < 5; j++)
            {
                if (j == 0)
                    ans[i][j] = ans[i - 1][j];
                else
                    ans[i][j] = ans[i - 1][j] + ans[i][j - 1];
            }
        }
        return ans[n][4];
    }
};
// @lc code=end
