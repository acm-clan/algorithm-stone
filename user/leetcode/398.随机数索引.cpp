/*
 * @lc app=leetcode.cn id=398 lang=cpp
 *
 * [398] 随机数索引
 */

// @lc code=start
class Solution {
public:
    Solution(vector<int>& nums) {
        this->nums = nums;
    }
    
    int pick(int target) {
        int cnt = 0;
        int index = -1;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == target) {
                cnt++;
                if (rand() % cnt == 0) {
                    index = i; // 1/i prob
                }
            }
        }

        return index;
    }

private:
    vector<int> nums;
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */
// @lc code=end

