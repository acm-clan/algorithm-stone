/*
 * @lc app=leetcode.cn id=973 lang=cpp
 *
 * [973] 最接近原点的 K 个点
 */

#include <queue>
using namespace std;

// @lc code=start
class Solution {
public:
    struct Node{
        vector<int> points;
        int value;
    };
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        auto cmp = [](Node a, Node b){
            return a.value < b.value;
        };
        priority_queue<Node, vector<Node>, decltype(cmp)> q(cmp);
        for(auto &v : points){
            Node n;
            n.points = v;
            n.value = v[0]*v[0]+v[1]*v[1];
            q.push(n);
            if(q.size()>k){
                q.pop();
            }
        }
        vector<vector<int>> ret;
        while(q.size()){
            Node n = q.top();
            q.pop();
            ret.push_back(n.points);
        }
        return ret;
    }
};
// @lc code=end

