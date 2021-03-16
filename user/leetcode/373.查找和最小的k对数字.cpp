/*
 * @lc app=leetcode.cn id=373 lang=cpp
 *
 * [373] 查找和最小的K对数字
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<vector<int>> ret;
        vector<pair<int, pair<int, int>>> min_heap;
        for(int& v1 : nums1)
            for(int& v2 : nums2)
                min_heap.push_back(make_pair(-v1 - v2, make_pair(v1, v2)));
        make_heap(min_heap.begin(), min_heap.end());
        while(!min_heap.empty() && k--){
            pop_heap(min_heap.begin(), min_heap.end());
            ret.push_back({min_heap.back().second.first, min_heap.back().second.second});
            min_heap.pop_back();
        }
        return ret;
    }
};
// @lc code=end

