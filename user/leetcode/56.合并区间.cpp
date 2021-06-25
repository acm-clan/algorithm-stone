/*
 * @lc app=leetcode.cn id=56 lang=cpp
 *
 * [56] 合并区间
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& arr) {
        sort(arr.begin(),arr.end());
        vector<vector<int>>ans;
        int start=arr[0][0];
        int end=arr[0][1];
        for(int i=1;i<arr.size();i++){
            if(start<=arr[i][0] && arr[i][0]<=end){
                end=max(end,arr[i][1]);
            }
            else{
                ans.push_back({start,end});
                start=arr[i][0];
                end=arr[i][1];
            }
        }
        ans.push_back({start,end});
        return ans;
    }
};

// @lc code=end

