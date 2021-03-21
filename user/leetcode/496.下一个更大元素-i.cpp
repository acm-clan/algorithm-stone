/*
 * @lc app=leetcode.cn id=496 lang=cpp
 *
 * [496] 下一个更大元素 I
 */

// @lc code=start
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> v;
        for(auto k : nums1){
            int s = 0;
            int t = -1;
            for(auto j : nums2){
                if(j==k){
                    s = 1;
                }
                if(s == 1 && j>k){
                    t = j;
                    break;
                }
            }
            v.push_back(t);
        }
        return v;
    }
};
// @lc code=end

