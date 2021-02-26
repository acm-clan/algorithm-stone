/*
 * @lc app=leetcode.cn id=563 lang=cpp
 *
 * [563] 二叉树的坡度
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int res = 0;
    int sum(TreeNode* t){
        if(!t)return 0;
        int l = sum(t->left);
        int r = sum(t->right);
        res += abs(l-r);
        return l+r+t->val;
    }
    int findTilt(TreeNode* t) {
        sum(t);
        return res;
    }
};
// @lc code=end

