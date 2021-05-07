/*
 * @lc app=leetcode.cn id=1604 lang=cpp
 *
 * [1604] 警告一小时内使用相同员工卡大于等于三次的人
 */

#include <algorithm>
#include <iostream>
#include <queue>
#include <unordered_map>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<string> alertNames(vector<string>& keyName, vector<string>& keyTime)
    {
        unordered_map<string, vector<int>> dict;
        int size = keyName.size();

        for (int idx = 0; idx < size; ++idx) {
            int h1 = keyTime[idx][0];
            int h2 = keyTime[idx][1];
            int m1 = keyTime[idx][3];
            int m2 = keyTime[idx][4];
            // 转换成数字
            dict[keyName[idx]].push_back((h1 * 10 + h2) * 60 + (m1 * 10 + m2));
        }

        vector<string> res;

        for (auto& [name, times] : dict) {
            if (times.size() <= 2) {
                continue;
            }

            sort(times.begin(), times.end());
            int k = 2;
            for (int idx = 2; idx < times.size(); ++idx) {
                // 关键点
                if (times[idx] - times[idx - 2] <= 60) {
                    res.push_back(name);
                    break;
                }
            }
        }

        sort(res.begin(), res.end());

        return res;
    }
};
// @lc code=end
