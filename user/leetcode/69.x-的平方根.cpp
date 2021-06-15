/*
 * @lc app=leetcode.cn id=69 lang=cpp
 *
 * [69] x 的平方根
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
    int mySqrt(int x) {
        int64_t l = 0, r = x;
        int64_t ans = 0;

        while(l<=r){
            int64_t mid = l+(r-l)/2;
            if(mid*mid <= x){
                ans = mid;
                l = mid+1;
            }else{
                r = mid-1;
            }
        }
        return ans;
    }
};
// @lc code=end

