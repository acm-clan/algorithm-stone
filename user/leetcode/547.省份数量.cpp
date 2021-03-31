/*
 * @lc app=leetcode.cn id=547 lang=cpp
 *
 * [547] 省份数量
 */
#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;


// @lc code=start
class Solution {
public:
    int Find(vector<int>& group, int index) {
        if (group[index] != index) {
            group[index] = Find(group, group[index]);
        }
        return group[index];
    }

    void Union(vector<int>& group, int index1, int index2) {
        group[Find(group, index1)] = Find(group, index2);
    }

    int findCircleNum(vector<vector<int>>& isConnected) {
        int count = isConnected.size();
        vector<int> group(count);

        for (int i = 0; i < count; i++) {
            group[i] = i;
        }
        for (int i = 0; i < count; i++) {
            for (int j = i + 1; j < count; j++) {
                if (isConnected[i][j] == 1) {
                    Union(group, i, j);
                }
            }
        }
        int circles = 0;
        for (int i = 0; i < count; i++) {
            if (group[i] == i) {
                circles++;
            }
        }
        return circles;
    }
};
// @lc code=end

