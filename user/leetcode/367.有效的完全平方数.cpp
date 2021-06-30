/*
 * @lc app=leetcode.cn id=367 lang=cpp
 *
 * [367] 有效的完全平方数
 */
#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

// @lc code=start
class Solution {
public: 
    bool isPerfectSquare(int num) {
        int64_t l=0, r=num;
        int64_t ans=r;
        while(l<=r){
            int64_t m = l + (r-l)/2;
            if(m*m >= num){
                r = m-1;
                ans = m;
            }else{
                l = m+1;
            }
        }
        printf("ans %d\n", ans);
        return ans*ans == num;
    }
};
// @lc code=end

