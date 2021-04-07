/*
 * @lc app=leetcode.cn id=1367 lang=cpp
 *
 * [1367] 二叉树中的列表
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
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
    //进行连续的检索
    bool dfs(ListNode*curr,TreeNode*root){
        if(curr==nullptr) return true;
        if(root==nullptr) return false;
        if(curr->val==root->val) return (dfs(curr->next,root->left)||dfs(curr->next,root->right));
        return false;
    }

    //枚举选择起点
    bool isSubPath(ListNode* head, TreeNode* root) {
        if(root==nullptr) return false;
        return dfs(head,root) || isSubPath(head,root->left) ||isSubPath(head,root->right);
    }
};
// @lc code=end