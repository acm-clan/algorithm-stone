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
        // 默认为0
        vector<int> res(arr.size(), 0);
        // 栈里面存放当前的索引位置,arr[st.top()]可以获得对应的数组值
        stack<int> indexes;

        for (int i = 0; i < arr.size(); ++i) {
            // 如果当前元素大于栈顶元素，说明需要让栈顶出栈
            while (!indexes.empty() && arr[i] > arr[indexes.top()]) {
                auto index = indexes.top();
                indexes.pop();
                // 当前的索引位置-栈顶元素的索引位置
                res[index] = i - index;
            }
            indexes.push(i);
        }
        return res;
    }
};
// @lc code=end
