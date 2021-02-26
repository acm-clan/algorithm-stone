/*
 * @lc app=leetcode.cn id=637 lang=cpp
 *
 * [637] 二叉树的层平均值
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

#include <queue>
using namespace std;

class Solution {
public:
    vector<double> averageOfLevels(TreeNode* root) {
        if(!root)return {};
        queue<TreeNode*> q;
        int c = 1;
        vector<double> levels;
        q.push(root);
        while(c){
            int n = 0;
            double s = 0;
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
                s += f->val;
            }
            levels.push_back(s/c);
            c = n;
        }
        return levels;
    }
};
// @lc code=end

