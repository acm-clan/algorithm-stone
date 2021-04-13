#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        short, long = len(s), len(t)
        i = 0
        j = 0
        while (i<short and j<long):
            if s[i]==t[j]:
                i+=1
            j+=1
        return i == short
# @lc code=end

