/*
 * @lc app=leetcode.cn id=855 lang=cpp
 *
 * [855] 考场就座
 */

#include <iostream>
#include <vector>
#include <queue>
#include <unordered_map>
#include <set>
#include <algorithm>
using namespace std;

// @lc code=start
class ExamRoom {
private:
    int n;
    set<int> s;
public:
    ExamRoom(int N) {
        n = N;
    }
    
    int seat() {
        if(s.empty()){
            s.insert(0);
            return 0;
        }
        int pos = 0, pre = -1, maxDist = 0;
        for(int cur : s){
            int dist = (cur - pre) / 2;
            if(dist > maxDist){
                pos = pre == -1 ? 0 : pre + dist;
                maxDist = dist;
            }
            pre = cur;
        }
        if(n - pre - 1 > maxDist){
            pos = n - 1;
        }
        s.insert(pos);
        return pos;
    }
    
    void leave(int p) {
        s.erase(p);
    }
};

/**
 * Your ExamRoom object will be instantiated and called as such:
 * ExamRoom* obj = new ExamRoom(N);
 * int param_1 = obj->seat();
 * obj->leave(p);
 */
// @lc code=end

