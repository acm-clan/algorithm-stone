/*
 * @lc app=leetcode.cn id=100 lang=cpp
 *
 * [100] 相同的树
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
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if((p == nullptr && q != nullptr) || (p != nullptr && q == nullptr)){
            return false;
        }
        if(p == nullptr && q == nullptr){
            return true;
        }
        if(p->val != q->val){
            return false;
        }
        bool l = isSameTree(p->left, q->left);
        if(!l){
            return false;
        }
        return isSameTree(p->right, q->right);
    }
};
// @lc code=end

