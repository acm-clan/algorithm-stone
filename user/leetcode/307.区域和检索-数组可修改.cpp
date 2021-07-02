/*
 * @lc app=leetcode.cn id=307 lang=cpp
 *
 * [307] 区域和检索 - 数组可修改
 */

#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

// @lc code=start
class NumArray {
public:
    int n;
    int *tree;
    int lowbit(int x)
    {
        return x&-x;
    }
    int query(int x)
    {
        int ans=0;
        for(int i=x;i>0;i-=lowbit(i))
        {
            ans+=tree[i];
        }
        return ans;
    }
    void add(int x,int u)
    {
        for(int i=x;i<=n;i+=lowbit(i))
        {
            tree[i]+=u;
        }
    }
    
    vector<int> vec;
    NumArray(vector<int>& nums) {
        n=nums.size();
        vec.assign(nums.begin(),nums.end());
        tree=new int[n+1]();
        for(int i=0;i<n;++i)
        {
            add(i+1,vec[i]);
        }
    }
    
    void update(int index, int val) {
        add(index+1,val-vec[index]);
        vec[index]=val;
    }
    
    int sumRange(int left, int right) {
        return query(right+1)-query(left);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
// @lc code=end
