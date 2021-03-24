/*
 * @lc app=leetcode.cn id=239 lang=cpp
 *
 * [239] 滑动窗口最大值
 */

// @lc code=start
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k)
    {
        int n = nums.size();
        deque<int> q;
        vector<int> res;
        for (int i = 0; i < n; ++i) {
            while (!q.empty() && nums[i] >= nums[q.back()])
                q.pop_back();
            q.push_back(i);
            if (i - q.front() + 1 > k)
                q.pop_front();
            if (i >= k - 1)
                res.push_back(nums[q.front()]);
        }
        return res;
    }
};
// @lc code=end
