/*
 * @lc app=leetcode.cn id=112 lang=cpp
 * 1
 * 2 null
 * 3 
 * [112] 路径总和
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
    bool sum(TreeNode* t, int targetSum) {
        if(!t->left && !t->right){
            return targetSum == t->val;
        }
        
        if(t->left && t->right){
            return sum(t->left, targetSum-t->val) || 
                sum(t->right, targetSum-t->val);
        }
        
        if(t->left){
            return sum(t->left, targetSum-t->val);
        }

        return sum(t->right, targetSum-t->val);
    }

    bool hasPathSum(TreeNode* t, int targetSum) {
        if(!t){
            return false;
        }

        return sum(t, targetSum);
    }
};
// @lc code=end

