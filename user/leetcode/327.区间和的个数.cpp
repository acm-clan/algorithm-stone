/*
 * @lc app=leetcode.cn id=327 lang=cpp
 *
 * [327] 区间和的个数
 */

// @lc code=start
class Solution {
public:
    
struct TreapNode{
    int pri;
    int key;
    TreapNode * son[2];
    int size;
    int num;
    
    TreapNode(int x){
        key = x;
        pri = rand();
        son[0] = son[1] = NULL;
        size = 1;
        num = 1;
    }
};


TreapNode * root;

void rotate(TreapNode * &r, int d){
    TreapNode * k = r->son[d^1];
    r->son[d^1] = k->son[d];
    int ori = r->size;
    int t = k->son[d^1] ? k->son[d^1]->size:0;
    r->size -= 1+t;
    k->son[d] = r;
    k->size = ori;
    
    r = k;
}

void insert(TreapNode * &r, int x){
    if(!r) r = new TreapNode(x);
    else{
        r->size ++;
        
        if(r->key == x){
            r->num ++;
            return;
        }
        
        int d = r->key < x;
        insert(r->son[d],x);
        
        if(r->son[d]->pri > r->pri)
            rotate(r,d^1);
    }
}

int getLeft(TreapNode * r){
    if(!r) return 0;
    if(r->son[0]) return r->num + r->son[0]->size;
    return r->num;
}

int find(TreapNode * r, long long x){
    if(!r) return 0;
    
    if(r->key == x) return getLeft(r);
    else if(r->key > x) return find(r->son[0],x);
    else    return getLeft(r)+find(r->son[1],x);
}

    long long sum[210001];
    
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        int ans = 0;
        int len = nums.size();
        if(!len) return 0;
        
        sum[0] = (long long)nums[0];
        for(int i=1;i<len;i++){
            sum[i] = sum[i-1] + (long long) nums[i];
        }
        
        
        for(int i=0;i<len;i++){
            long long n = sum[i];
            ans += find(root,n-lower) - find(root,n-upper-1);
            insert(root,n);
            if(n <= upper && n >= lower) ans ++;
        }
        return ans;
    }
};
// @lc code=end

