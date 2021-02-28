/*
 * @lc app=leetcode.cn id=114 lang=cpp
 *
 * [114] 二叉树展开为链表
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

#include <vector>
using namespace std;

class Solution {
public:
    vector<TreeNode*> nodes;
    // 使用一个数组宝存顺序
    void travel(TreeNode* root){
        if(!root)return;
        nodes.push_back(root);
        travel(root->left);
        travel(root->right);
    }
    void flatten(TreeNode* root) {
        travel(root);
        
        TreeNode* p = root;
        for(auto k: nodes){
            k->left = 0;
            k->right = 0;
            if(k==root)continue;

            p->right = k;
            p->left = 0;
            p = k;
        }
    }
};
// @lc code=end

