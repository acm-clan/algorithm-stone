/*
 * @lc app=leetcode.cn id=703 lang=cpp
 *
 * [703] 数据流中的第 K 大元素
 */

// @lc code=start
class KthLargest {
public:
    vector<int> n;
    int target = 0;
    int v = 0;
    KthLargest(int k, vector<int>& nums) {
        target = k;
        n = nums;
        std::sort(n.begin(), n.end());
        v = n[k-1];
    }
    
    int add(int val) {
        if(val <)
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
// @lc code=end

