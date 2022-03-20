/*
 * @lc app=leetcode.cn id=49 lang=cpp
 *
 * [49] 字母异位词分组
 */

#include <vector>
#include <algorithm>
using namespace std;

// @lc code=start
class Solution {
public:
    long long coutPairs(vector<int>& nums, int k) {
        // 取得最大数字m
        int m = *max_element(nums.begin(), nums.end());
        // 创建2个数组
        vector<long long> cnt(m + 1), s(m + 1);
        //统计数字x出现的次数
        for (int x : nums) cnt[x] += 1;

        // 计算数字i的倍数的数量，比如2，那么2、4、6、8...所有数字的数量
        for (int i = 1; i <= m; i += 1)
            for (int j = i; j <= m; j += i) {
                s[i] += cnt[j];
            }
        long long ans = 0;
        for (int i = 1; i <= m; i += 1) {
            // 计算k-24 i-18最大公约数是6，k剩余部分是3
            // k-4 i-6
            int x = k / gcd(k, i);
            if (x <= m) ans += cnt[i] * s[x];
        }
        // 
        for (long long i = 1; i <= m; i += 1)
            if ((long long)i * i % k == 0) ans -= cnt[i];
        return ans / 2;
    }
};
// @lc code=end

