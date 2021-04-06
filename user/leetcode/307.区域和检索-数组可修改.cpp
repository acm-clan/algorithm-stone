/*
 * @lc app=leetcode.cn id=307 lang=cpp
 *
 * [307] 区域和检索 - 数组可修改
 */

// @lc code=start
class NumArray {
public:
    vector<int> arr;
    vector<int> sum, change, upda, lazy;
    int n;
    NumArray(vector<int>& nums) {
        n = nums.size();
        arr = vector<int> (n + 1);
        sum = vector<int> (n << 2);
        change = vector<int> (n << 2);
        upda = vector<int> (n << 2);
        lazy = vector<int> (n << 2);
        for(int i=1;i<=n;i++) arr[i] = nums[i-1];
        build(1,n,1);
    }

    void build(int l,int r, int rt) {
        if(l==r) {
            sum[rt] = arr[l];
            return ;
        }
        int mid = (l+r) >> 1;
        build(l,mid,rt<<1);
        build(mid+1,r,rt<<1 | 1);
        pushUp(rt);
    }

    void pushUp(int rt) {
        sum[rt] = sum[rt<<1] + sum[rt<<1 | 1];
    }

    void add(int L, int R, int C, int l, int r, int rt) {
        if(L<=l && r<=R) {
            sum[rt] += C * (r-l+1);
            lazy[rt] += C;
            return ;
        }

        int mid = (l+r) >> 1;
        pushDown(rt, mid-l+1,r-mid);
        if(L<=mid) add(L,R,C,l,mid,rt<<1);
        if(R>mid) add(L,R,C,mid+1,r,rt<<1|1);
        pushUp(rt);
    }

    void Update(int L, int R, int C, int l, int r, int rt) {
        if(L<=l && r<=R) {
            upda[rt] = true;
            change[rt] = C;
            sum[rt] = C * (r-l+1);
            lazy[rt] = 0;
            return ;
        }

        int mid = (l+r) >> 1;
        pushDown(rt, mid-l+1,r-mid);
        if(L<=mid) Update(L,R,C,l,mid,rt<<1);
        if(R>mid) Update(L,R,C,mid+1,r,rt<<1|1);
        pushUp(rt);
    }

    void pushDown(int rt, int ln, int rn) {
        if(upda[rt]){
            upda[rt<<1] = 1;
            upda[rt<<1 | 1] = 1;
            change[rt<<1] = change[rt];
            change[rt<<1 | 1] = change[rt];
            lazy[rt<<1] = 0;
            lazy[rt<<1|1] = 0;
            sum[rt<<1] = change[rt] * ln;
            sum[rt<<1 | 1] = change[rt] * rn;
            upda[rt] = 0;
        }
        if(lazy[rt]) {
            lazy[rt<<1] += lazy[rt];
            lazy[rt<<1 | 1] += lazy[rt];
            sum[rt<<1] += lazy[rt] * ln;
            sum[rt<<1|1] += lazy[rt] * rn;
            lazy[rt] = 0;
        }
    }
    
    int query(int L, int R, int l, int r, int rt){
        if(L<=l && r<=R) return sum[rt];
        int mid = (l+r) >> 1;
        pushDown(rt, mid-l+1, r-mid);
        int ans = 0;
        if(L<=mid) ans+=query(L,R,l,mid,rt<<1);
        if(R>mid) ans += query(L,R,mid+1,r,rt<<1|1);
        return ans;
    }

    void update(int i, int val) {
        Update(i+1,i+1,val,1,n,1);
    }
    
    int sumRange(int i, int j) {
        return query(i+1,j+1,1,n,1);
    }
};


/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
// @lc code=end

