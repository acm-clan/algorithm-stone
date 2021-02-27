/*
 * @lc app=leetcode.cn id=94 lang=cpp
 *
 * [94] 二叉树的中序遍历
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
    void travel(TreeNode* t, vector<int> & v){
        if(!t)return;
        travel(t->left, v);
        // 
        v.push_back(t->val);
        travel(t->right, v);
    }
    vector<int> inorderTraversal(TreeNode* t) {
        vector<int> v;
        travel(t, v);
        return v;
    }
};
// @lc code=end

