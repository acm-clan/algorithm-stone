/*
 * @lc app=leetcode.cn id=201 lang=cpp
 *
 * [201] 数字范围按位与
 */

// @lc code=start
class Solution {
public:
    int rangeBitwiseAnd(int left, int right) {
        int i = 1;
        if (left == right) {
            return left;
        }
        if (left == 0 ) {
            return 0;
        }

        if (left >= 1073741824) {
            return 1073741824 + rangeBitwiseAnd(left-(1073741824), right-(1073741824));
        }

        i = 1;
        while (left >= i) {
            i *= 2;
        }

        if (right >= i) {
            return 0;
        }
        else {
            return i/2 + rangeBitwiseAnd(left-(i/2), right-(i/2));
        }
    }
};

// @lc code=end

