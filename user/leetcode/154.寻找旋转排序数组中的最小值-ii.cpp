/*
 * @lc app=leetcode.cn id=154 lang=cpp
 *
 * [154] 寻找旋转排序数组中的最小值 II
 */

// @lc code=start
class Solution {
public:
    int findMin(vector<int>& nums) {
        int low = 0;
        int high = nums.size() - 1;
        while (low < high) {
            int m = low + (high - low) / 2;
            if (nums[m] < nums[high]) {
                high = m;
            }
            else if (nums[m] > nums[high]) {
                low = m + 1;
            }
            else {
                high -= 1;
            }
        }
        return nums[low];
    }
};
// @lc code=end

