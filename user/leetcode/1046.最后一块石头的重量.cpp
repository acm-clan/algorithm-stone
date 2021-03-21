/*
 * @lc app=leetcode.cn id=1046 lang=cpp
 *
 * [1046] 最后一块石头的重量
 */
#include <queue>
using namespace std;

// @lc code=start
class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> q;
        for(auto v: stones){
            q.emplace(v);
        }
        while(q.size()>=2){
            int a = q.top();
            q.pop();
            int b = q.top();
            q.pop();
            q.emplace(abs(a-b));
        }
        return q.size()?q.top():0;
    }
};
// @lc code=end

