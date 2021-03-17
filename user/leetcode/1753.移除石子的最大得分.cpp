/*
 * @lc app=leetcode.cn id=1753 lang=cpp
 *
 * [1753] 移除石子的最大得分
 */

// @lc code=start
class Solution {
public:
    int maximumScore(int a, int b, int c) {
        priority_queue<int> q;
        int ans = 0;
        q.push(a);
        q.push(b);
        q.push(c);
        while(true){
            int max_num = q.top();
            q.pop();
            int medium = q.top();
            q.pop();
            int min_num = q.top();
            if(!medium)break; //结束条件
            int temp = max(medium - min_num, 1); //我要从最多的两堆里拿多少
            max_num -= temp;
            medium -= temp;
            ans += temp; //更新答案
            q.push(max_num);
            q.push(medium);
        }
        return ans;
    }
};
// @lc code=end

