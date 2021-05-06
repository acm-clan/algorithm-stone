/*
 * @lc app=leetcode.cn id=220 lang=cpp
 *
 * [220] 存在重复元素 III
 */

#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

// @lc code=start
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& n, int k, int t)
    {
        set<long> st;
        for (int i = 0; i < n.size(); i++) {
            // 找一个在区间n[i]-t到n[i]+t的数
            // 查找大于等于n[i]-t的值
            auto lb = st.lower_bound((long)n[i] - t);
            // 必须小于n[i]+t的值
            if (lb != st.end() && *lb <= (long)n[i] + t)
                return 1;
            // 滑动窗口大小为k
            st.insert(n[i]);
            if (i >= k)
                st.erase(n[i - k]);
        }
        return 0;
    }
};
// @lc code=end
