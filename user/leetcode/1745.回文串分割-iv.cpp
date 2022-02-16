/*
 * @lc app=leetcode.cn id=1745 lang=cpp
 *
 * [1745] 回文串分割 IV
 */
#include <string>
using namespace std;

// @lc code=start
class Solution {
public:
  bool checkPartitioning(string s) {
    int n = s.size(), maxl = 0, r = 0, c = 0, len[2 * n + 1], len1[n];
    string _s(2 * n + 1, '*');
    for (int i = 0; i < n; i++)
      _s[2 * i + 1] = s[i];
      
    for (int i = 0; i < 2 * n + 1; i++) {
      len[i] = i < r ? min(r - i + 1, len[2 * c - i]) : 1;
      while (i + len[i] < 2 * n + 1 && i - len[i] >= 0 &&
             _s[i + len[i]] == _s[i - len[i]])
        len[i]++;
      if (i + len[i] - 1 >= r) {
        r = i + len[i] - 1;
        c = i;
      }
    }
    int idx = 0;
    for (int i = 1; i < 2 * n + 1 && idx < n; i += 2) {
      while (idx < n && idx <= i / 2 + len[i] / 2 - 1) {
        len1[idx] = idx - i / 2 + idx - i / 2 + 1;
        idx++;
      }
      while (idx < n && idx <= i / 2 + len[i + 1] / 2) {
        len1[idx] = idx - i / 2 + idx - i / 2;
        idx++;
      }
    }
    for (int i = 0; i < n - 1; i++) {
      if (n - len[i + n + 1] < i + 2) {
        if (i - len1[i] >= 0 && len1[i - len1[i]] == i - len1[i] + 1 ||
            maxl && i - len[i + maxl + 1] < maxl)
          return 1;
      }
      if (len1[i] == i + 1)
        maxl = i + 1;
    }
    return 0;
  }
};
// @lc code=end
