/*
 * @lc app=leetcode.cn id=215 lang=cpp
 *
 * [215] 数组中的第K个最大元素
 */
#include <queue>
using namespace std;

// @lc code=start
class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        // 用小堆
        priority_queue<int, vector<int>, greater<int>> q;
        for(auto v : nums){
            q.push(v);
            if(q.size()>k){
                q.pop();
            }
        }
        return q.top();
    }
};
// @lc code=end

