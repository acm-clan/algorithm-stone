/*
 * @lc app=leetcode.cn id=857 lang=cpp
 *
 * [857] 雇佣 K 名工人的最低成本
 */

// @lc code=start
class Solution {
public:
    double mincostToHireWorkers(vector<int>& quality, vector<int>& wage, int K)
    {
        vector<pair<double, int>> x;
        int N = quality.size();
        for (int i = 0; i < N; i++)
            x.push_back({ wage[i] * 1.0 / quality[i] * 1.0, quality[i] });
        sort(x.begin(), x.end());
        double res = INT_MAX, temp = 0.0;
        priority_queue<int> heap;
        for (auto worker : x) {
            heap.push(worker.second);
            temp += worker.second;
            if (heap.size() > K) {
                temp -= heap.top();
                heap.pop();
            }
            if (heap.size() == K)
                res = min(res, temp * worker.first);
        }
        return res;
    }
};
// @lc code=end
