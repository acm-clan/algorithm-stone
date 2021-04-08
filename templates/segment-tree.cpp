#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

// @lc code=start
class NumArray {
public:
    struct TreeNode{
        int l, r, v;
        TreeNode * left = nullptr;
        TreeNode * right = nullptr;
        TreeNode(int l, int r, int v):l(l), r(r), v(v){

        }
        TreeNode(int l, int r, int v, TreeNode * left, TreeNode * right):l(l), r(r), v(v),
            left(left), right(right)
        {

        }
    };

    TreeNode * root;

    TreeNode * buildTree(vector<int>& nums, int l, int r)
    {
        if(l == r){
            // 叶子节点
            return new TreeNode(l, r, nums[l]);
        }

        // 后序构造
        auto left = buildTree(nums, l, (l+r)/2);
        auto right = buildTree(nums, (l+r)/2+1, r);

        // 非叶子节点
        return new TreeNode(l, r, left->v+right->v, left, right);
    }

    void dumpInternal(TreeNode * n, int d){
        if(!n)return;
        for(int i=0; i<d; i++)printf("--");
        printf("%d(%d %d)\n", n->v, n->l, n->r);
        dumpInternal(n->left, d+1);
        dumpInternal(n->right, d+1);
    }

    void updateNode(TreeNode * n, int pos, int val){
        if(!n)return;

        if(n->l == n->r && n->l == pos){
            n->v = val;
            return;
        }

        int m = (n->l+n->r)/2;

        // 后序遍历
        if(pos <= m){
            updateNode(n->left, pos, val);
        }else{
            updateNode(n->right, pos, val);
        }
        n->v = n->left->v + n->right->v;
    }

    int query(TreeNode * n, int l, int r){
        if(!n)return 0;
        
        if(n->l == l && n->r == r){
            return n->v;
        }

        int m = (n->l + n->r)/2;

        // 左右
        if(r <= m){
            return query(n->left, l, r);
        }else if(l > m){
            return query(n->right, l, r);
        }

        // 跨区间
        return query(n->left, l, m) + query(n->right, m+1, r);
    }

    void dump(TreeNode * n){
        // dumpInternal(n, 1);
    }

    NumArray(vector<int>& nums)
    {
        root = buildTree(nums, 0, nums.size()-1);
        dump(root);
    }

    void update(int pos, int val)
    {
        updateNode(root, pos, val);
        dump(root);
    }

    int sumRange(int l, int r)
    {
        return query(root, l, r);
    }
};
