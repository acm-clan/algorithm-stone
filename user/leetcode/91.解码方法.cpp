/*
 * @lc app=leetcode.cn id=91 lang=cpp
 * 1210340156
 * 
 * [91] 解码方法
 */

// @lc code=start
class Solution {
public:
    int numDecodings(string s) {
        int n = s.length();
        int f[n+1];
        f[0] = 1;
        for(int i=2; i<=n; i++){
            // single
            if(s[i-1] != '0'){
                f[i] += f[i-1];
            }
            
            // double
            f[i] += f[i-2];
        }
        return 0;
    }
};
// @lc code=end

