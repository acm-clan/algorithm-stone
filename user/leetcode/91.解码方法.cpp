/*
 * @lc app=leetcode.cn id=91 lang=cpp
 * 1210340156
 * 
 * [91] 解码方法
 */
#include <string>
using namespace std;

// @lc code=start
class Solution {
public:
    int numDecodings(string s) {
        int n = s.length();
        if(n == 0) return 0;
        int f[n+1];
        f[0] = 1;
        f[1] = s[0] == '0'?0:1;
        // 思路很简单，一个数字直接加，2个数字判断是不是10到26
        for(int i=2; i<=n; i++){
            // single
            if(s[i-1] != '0'){
                f[i] = f[i-1];
            }
            // double
            int two = (s[i-2]-'0')*10 + s[i-1]-'0';
            if(two >= 10 && two <= 26){
                f[i] += f[i-2];
            }
        }
        return f[n];
    }
};
// @lc code=end

