/*
 * @lc app=leetcode.cn id=621 lang=cpp
 *
 * [621] 任务调度器
 */

// @lc code=start
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> Task(26, 0);
        int res = 0, restSpace = 0;
        for (char t : tasks) {
            Task[t - 'A']++;
        }
        
        // 最后一个最大
        sort(Task.begin(), Task.end());
        
        restSpace = n * (Task[25] - 1);
        res = Task[25] + (Task[25] - 1) * n;  

        for (int i=24; i>=0; i--) {
            if (Task[i] == Task[25]) {
                if (restSpace > 0) {
                    res++;
                    restSpace -= Task[25] - 1;
                }
                else res += Task[25];
            } else {
                if (restSpace >= Task[i]) restSpace -= Task[i];
                else {
                    res += Task[i] - restSpace;
                    restSpace = 0;
                }
            }
        }
        return res;
    }
};
// @lc code=end

