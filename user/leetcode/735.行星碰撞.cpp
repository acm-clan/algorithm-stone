/*
 * @lc app=leetcode.cn id=735 lang=cpp
 *
 * [735] 行星碰撞
 */
#include <queue>
using namespace std;

// @lc code=start
class Solution {
public:
    vector<int> asteroidCollision(vector<int>& asteroids)
    {
        vector<int> ans;
        int n = asteroids.size();
        for (int i = 0; i < n; ++i) {
            if (ans.empty() || asteroids[i] > 0) {
                ans.push_back(asteroids[i]);
            } else {
                while (ans.size() && ans.back() > 0 && ans.back() < -asteroids[i])
                    ans.pop_back();
                if (ans.empty() || ans.back() < 0)
                    ans.push_back(asteroids[i]);
                else if (ans.back() == -asteroids[i])
                    ans.pop_back();
            }
        }
        return ans;
    }
};
// @lc code=end
