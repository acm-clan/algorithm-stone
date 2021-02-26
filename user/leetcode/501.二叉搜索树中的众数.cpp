/*
 * @lc app=leetcode.cn id=501 lang=cpp
 *
 * [501] 二叉搜索树中的众数
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
    int n = -1;
    int count = 0;
    int maxCount=0;
    int maxN=0;
    vector<int> v;
    void travel(TreeNode * t){
        if(!t)return;
        travel(t->left);
        //
        if(n == -1){
            n = t->val;
        }
        if(t->val == n){
            ++count;
            if(count > maxCount){
                maxCount = count;
                maxN = n;
                v.clear();
            }
        }else{
            if(count == maxCount){
                v.push_back(n);
            }
            count = 1;
            n = t->val;
        }
        travel(t->right);
    }
    vector<int> findMode(TreeNode* root) {
        if(!root)return {};
        travel(root);
        if(count == maxCount){
            v.push_back(n);
        }
        return v;
    }
};
// @lc code=end

