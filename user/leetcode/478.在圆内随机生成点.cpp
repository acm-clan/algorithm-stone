/*
 * @lc app=leetcode.cn id=478 lang=cpp
 *
 * [478] 在圆内随机生成点
 */

// @lc code=start
class Solution {
public:
    double r, x_cen, y_cen;
    Solution(double radius, double x_center, double y_center) {
        r = radius;
        x_cen = x_center;
        y_cen = y_center;
    }
    
    vector<double> randPoint() {
        while (true) {
            double x = (2 * (double)rand() / RAND_MAX - 1.0) * r;
            double y = (2 * (double)rand() / RAND_MAX - 1.0) * r;
            if (x * x + y * y <= r * r) return {x_cen + x, y_cen + y}; 
        }
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(radius, x_center, y_center);
 * vector<double> param_1 = obj->randPoint();
 */
// @lc code=end

