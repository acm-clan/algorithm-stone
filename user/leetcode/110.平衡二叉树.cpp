/*
 * @lc app=leetcode.cn id=110 lang=cpp
 *
 * [110] 平衡二叉树
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
    int depth(TreeNode* t){
        if(!t)return 0;
        return max(depth(t->left), depth(t->right))+1;
    }
    bool isBalanced(TreeNode* t) {
        if(!t)return true;
        int l = depth(t->left);
        int r = depth(t->right);
        if(abs(l-r) > 1){
            return false;
        }
        return isBalanced(t->left) && isBalanced(t->right);
    }
};
// @lc code=end

