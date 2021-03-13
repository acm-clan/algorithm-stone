/*
 * @lc app=leetcode.cn id=933 lang=cpp
 *
 * [933] 最近的请求次数
 */
#include<queue>
using namespace std;

// @lc code=start
class RecentCounter {
public:
    queue<int> q;
    RecentCounter() {

    }
    
    int ping(int t) {
        q.push(t);
        // 取出超过3000的数值，只保留3000以内的
        while(q.front() < t-3000){
            q.pop();
        }
        return q.size();
    }
};

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter* obj = new RecentCounter();
 * int param_1 = obj->ping(t);
 */
// @lc code=end

