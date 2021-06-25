/*
 * @lc app=leetcode.cn id=435 lang=cpp
 *
 * [435] 无重叠区间
 */

// @lc code=start
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(),intervals.end(),[](vector<int>& l,vector<int>& r){return l[1]<r[1];});
        int count=0;
        int len=intervals.size();
        int left=0;
        for(int i=0;i<len;++i){
            if(i==0||intervals[i][0]>=left){
                ++count;
                left=intervals[i][1];
            }
        }
        return len-count;
    }
};

// @lc code=end

