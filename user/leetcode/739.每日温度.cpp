/*
 * @lc app=leetcode.cn id=739 lang=cpp
 *
 * [739] 每日温度
 */

#include <iostream>
#include <map>
#include <queue>
#include <stack>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <unordered_set>

using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& arr)
    {
        int n = arr.size();
        vector<int> res(n, 0);
        // 栈里面存放当前的索引位置
        stack<int> st;

        for (int i = 0; i < arr.size(); ++i) {
            // 如果当前元素大于栈顶元素，说明需要让栈顶出栈
            while (!st.empty() && arr[i] > arr[st.top()]) {
                auto t = st.top();
                st.pop();
                // 距离就是当前位置
                res[t] = i - t;
            }
            st.push(i);
        }
        return res;
    }
};
// @lc code=end
