/*
 * @lc app=leetcode.cn id=102 lang=cpp
 *
 * [102] 二叉树的层序遍历
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

#include <queue>
using namespace std;

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if(!root)return {};
        queue<TreeNode*> q;
        int c = 1;
        vector<vector<int>> levels;
        q.push(root);
        while(c){
            int n = 0;
            vector<int> layer;
            for(int i=0; i<c; i++){
                auto f = q.front();
                q.pop();
                if(f->left){
                    q.push(f->left);
                    n++;
                }
                if(f->right){
                    q.push(f->right);
                    n++;
                }
                layer.push_back(f->val);
            }
            c = n;
            levels.push_back(layer);
        }
        return levels;
    }
};
// @lc code=end

