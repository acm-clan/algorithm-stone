/*
 * @lc app=leetcode.cn id=4 lang=cpp
 *
 * [4] 寻找两个正序数组的中位数
 */
#include <algorithm>
#include <iostream>
#include <queue>
#include <set>
#include <vector>
using namespace std;

// @lc code=start
class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2)
    {
        // 时间O(nums1.size()+nums2.size())，空间O(1)
        vector<int> nums;
        int p1 = 0, p2 = 0, mid = (nums1.size() + nums2.size()) / 2;
        while ((p1 < nums1.size() || p2 < nums2.size()) && p1 + p2 <= mid) {
            if (p1 == nums1.size())
                nums.push_back(nums2[p2++]);
            else if (p2 == nums2.size())
                nums.push_back(nums1[p1++]);
            else
                nums.push_back(nums1[p1] < nums2[p2] ? nums1[p1++] : nums2[p2++]);
        }
        if ((nums1.size() + nums2.size()) % 2 == 1)
            return nums[mid];
        else
            return (nums[mid - 1] + nums[mid]) / 2.0;
    }
};
// @lc code=end
