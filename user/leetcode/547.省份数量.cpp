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
    // 寻找树根
    int Find(vector<int>& root, int index) {
        if (root[index] != index) {
            root[index] = Find(root, root[index]);
        }
        return root[index];
    }

    // 将一个根节点指向另一个根节点
    void Union(vector<int>& root, int index1, int index2) {
        root[Find(root, index1)] = Find(root, index2);
    }

    int findCircleNum(vector<vector<int>>& isConnected) {
        int size = isConnected.size();
        vector<int> root(size);

        // 初始指向自己
        for (int i = 0; i < size; i++) {
            root[i] = i;
        }
        //合并集合
        for (int i = 0; i < size; i++) {
            for (int j = i + 1; j < size; j++) {
                if (isConnected[i][j] == 1) {
                    Union(root, i, j);
                }
            }
        }
        //计算树的个数
        int circles = 0;
        for (int i = 0; i < size; i++) {
            if (root[i] == i) {
                circles++;
            }
        }
        return circles;
    }
};
// @lc code=end

