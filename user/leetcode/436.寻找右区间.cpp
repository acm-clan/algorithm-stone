/*
 * @lc app=leetcode.cn id=436 lang=cpp
 *
 * [436] 寻找右区间
 */

// @lc code=start
class Solution {
public:
    int findlocation(vector<pair<int, int>>& arr, int val) {
        int n = arr.size();

        if (val > arr[n - 1].first) {
            return -1;
        }
        int left = 0;
        int right = n - 1;

        while (left < right) {
            int mid = left + (right - left) / 2;
            if (arr[mid].first > val) {
                right = mid;
            } else if (arr[mid].first < val) {
                left = mid + 1;
            } else {
                return arr[mid].second;
            }
        }
        return arr[right].second;
    }

    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        vector<pair<int, int>> arr;
        vector<int> ans;

        int n = intervals.size();

        for (int i = 0; i < n; i++) {
            arr.push_back({intervals[i][0], i});
        }
        sort(arr.begin(), arr.end());

        for (int i = 0; i < n; i++) {
            ans.push_back(findlocation(arr, intervals[i][1]));
        }
        return ans;
    }
};
// @lc code=end

