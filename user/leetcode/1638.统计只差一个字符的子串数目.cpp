/*
 * @lc app=leetcode.cn id=1638 lang=cpp
 *
 * [1638] 统计只差一个字符的子串数目
 */

// @lc code=start
class Solution {
public:
    int countSubstrings(string s, string t) {
        int m = s.size();
        int n = t.size();
        int ans = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                int diff = 0;
                for (int k = 0; i + k < m && j + k < n; ++k) {
                    diff += (s[i + k] != t[j + k]);
                    if (diff > 1) {
                        break;
                    }
                    if (diff == 1) {
                        ++ans;
                    }
                }
            }
        }
        return ans;
    }
};
// @lc code=end

