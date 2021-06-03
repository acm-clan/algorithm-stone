/*
 * @lc app=leetcode.cn id=421 lang=cpp
 *
 * [421] 数组中两个数的最大异或值
 */

// @lc code=start
int dummy = [](){
    ios::sync_with_stdio(false);
    return 0;
}();

#define maxn 31*2*10000+4
int l[maxn], r[maxn];
int tail;
int ht;

class Solution {
    void insert(int num) {
        int f = 1 << (ht-1);
        
        int cur = 0;
        while (f) {
            if (f & num) {
                if (r[cur] == 0) {
                    r[cur] = tail++;
                    // n[tail++] = (f == 1);
                }
                cur = r[cur];
            } else {
                if (l[cur] == 0) {
                    l[cur] = tail++;
                    // n[tail++] = (f == 1);
                }
                cur = l[cur];
            }
            f >>= 1;
        }
    }

    int ans;

    void dfs(int fcur, int scur, int cht, int num) {
        ans = max(ans, num);
        if (cht == 0) {
            return;
        }
        
        if (cht < ht && (ans & (1<<cht)) && !(num & (1<<cht)))
            return;

        
        if (r[fcur]) {
            if (l[scur]) {
                dfs(r[fcur], l[scur], cht-1, num | (1<<(cht-1)));
            }
            else if (r[scur]) {
                dfs(r[fcur], r[scur], cht-1, num);
            }
        }

        if (l[fcur]) {
            if (r[scur]) {
                dfs(l[fcur], r[scur], cht-1, num | (1<<(cht-1)));
            } else if (l[scur]) {
                dfs(l[fcur], l[scur], cht-1, num);
            }
        }
    }


public:
    int findMaximumXOR(vector<int>& nums) {
        memset(l, 0, sizeof(l));
        memset(r, 0, sizeof(r)); 
        tail = 1;
        int len = nums.size();
        int nmax = 0;
        for (int i = 0; i < len; i++) 
            nmax |= nums[i];
        
        if (nmax == 0) return 0;

        // ht = floor(log2(nmax))+1;
        ht = 32 - __builtin_clz(nmax | 1);

        for (int i = 0; i < len; i++)
            insert(nums[i]);
        
        ans = 0;
        dfs(0, 0, ht, 0);
        return ans;
    }
};

// @lc code=end

