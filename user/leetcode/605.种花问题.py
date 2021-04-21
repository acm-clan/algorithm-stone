#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        s = 1
        t = 0
        for k in flowerbed:
            if k == 1:
                if t == 1:
                    n += 1
                    t = 0
                s = 0
            else:
                t = 0
                s += 1
            if s == 2:
                t = 1
                n -= 1
                s = 0
        return n <= 0
# @lc code=end
