/*
 * @lc app=leetcode.cn id=1642 lang=cpp
 *
 * [1642] 可以到达的最远建筑
 */

// @lc code=start
class Solution {
public:
    int furthestBuilding(vector<int>& heights, int bricks, int ladders) {
        int n = heights.size();
        // 由于我们需要维护最大的 l 个值，因此使用小根堆
        priority_queue<int, vector<int>, greater<int>> q;
        // 需要使用砖块的 delta h 的和
        int s = 0;
        for (int i = 1; i < n; ++i) {
            int d = heights[i] - heights[i - 1];
            if (d > 0) {
                q.push(d);
                // 如果优先队列已满，需要拿出一个其中的最小值，改为使用砖块
                if (q.size() > ladders) {
                    s += q.top();
                    q.pop();
                }
                if (s > bricks) {
                    return i - 1;
                }
            }
        }
        return n - 1;
    }
};
// @lc code=end

