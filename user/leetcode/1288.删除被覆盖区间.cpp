/*
 * @lc app=leetcode.cn id=1288 lang=cpp
 *
 * [1288] 删除被覆盖区间
 */

// @lc code=start
class Solution {
  public:
  int removeCoveredIntervals(vector<vector<int>>& intervals) {
    //   从左到右，左边相等取较大值
    sort(begin(intervals), end(intervals),
      [](const vector<int> &o1, const vector<int> &o2) {
      return o1[0] == o2[0] ? o2[1] < o1[1] : o1[0] < o2[0];
    });

    int count = 0;
    int end, prev_end = 0;
    for (auto curr : intervals) {
      end = curr[1];
      // 不包括范围加1   
      if (prev_end < end) {
        ++count;
        prev_end = end;
      }
    }
    return count;
  }
};
// @lc code=end

