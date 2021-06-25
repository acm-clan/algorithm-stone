/*
 * @lc app=leetcode.cn id=57 lang=cpp
 *
 * [57] 插入区间
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> res;
        // if (intervals.empty()) {
        //     res.push_back(newInterval);
        //     return res;
        // }
        int n = intervals.size();
        int i = 0;
        while (i < n && intervals[i][1] < newInterval[0]) {
            res.push_back(intervals[i]);
            i++;
        }
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(intervals[i][0], newInterval[0]);
            newInterval[1] = max(intervals[i][1], newInterval[1]);
            i++;
        }
        res.push_back(newInterval);
        for (int j = i; j < n; j++) {
            res.push_back(intervals[j]);
        }
        return res;
    }
};
// @lc code=end

