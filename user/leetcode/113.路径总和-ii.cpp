/*
 * @lc app=leetcode.cn id=113 lang=cpp
 *
 * [113] 路径总和 II
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
    vector<vector<int>> res;
    // 增加一个路径记录
    void travel(TreeNode* root, int targetSum, vector<int> & path){
        if(!root)return;
        if(!root->left && !root->right && targetSum == root->val){
            path.push_back(root->val);
            res.push_back(path);
            path.pop_back();
        }
        path.push_back(root->val);
        travel(root->left, targetSum - root->val, path);
        path.pop_back();
        path.push_back(root->val);
        travel(root->right, targetSum - root->val, path);
        path.pop_back();
    }

    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<int> path;
        travel(root, targetSum, path);
        return res;
    }
};
// @lc code=end

