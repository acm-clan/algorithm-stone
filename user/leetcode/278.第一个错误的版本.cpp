/*
 * @lc app=leetcode.cn id=278 lang=cpp
 *
 * [278] 第一个错误的版本
 */

// @lc code=start
// The API isBadVersion is defined for you.
// bool isBadVersion(int version);
#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int firstBadVersion(int n) {
        int64_t l=0, r=n;
        int64_t ans = n;
        
        while(l<=r){
            int64_t mid = (l+r)>>1;
            if(isBadVersion(mid)){
                ans = mid;
                r = mid - 1;
            }else{
                l = mid + 1;
            }
        }
        return ans;
    }
};
// @lc code=end

