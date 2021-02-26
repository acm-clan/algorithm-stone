/*
 * @lc app=leetcode.cn id=606 lang=cpp
 *
 * [606] 根据二叉树创建字符串
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
    string s;
    void travel(TreeNode* t){
        if(!t)return;
        s += std::to_string(t->val);

        if(t->left || t->right){
            s+="(";
            travel(t->left);
            s += ")";
        }

        if(t->right){
            s+="(";
            travel(t->right);
            s += ")";
        }
    }
    string tree2str(TreeNode* t) {
        travel(t);
        return s;
    }
};
// @lc code=end

