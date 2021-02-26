/*
 * @lc app=leetcode.cn id=543 lang=cpp
 *
 * [543] 二叉树的直径
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    int res = 0;
    int dep(TreeNode* t){
        if(!t)return 0;
        int l = dep(t->left);
        int r = dep(t->right);
        res = max(res, l+r);
        return max(l, r)+1;
    }
    int diameterOfBinaryTree(TreeNode* t) {
        dep(t);
        return res;
    }
};
// @lc code=end

