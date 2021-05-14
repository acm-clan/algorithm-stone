/*
 * @lc app=leetcode.cn id=1606 lang=cpp
 *
 * [1606] 找到处理最多请求的服务器
 */

// @lc code=start
typedef pair<int,int> pii;
class Solution {
public:
    vector<int> busiestServers(int k, vector<int>& arrival, vector<int>& load) {
        int n = arrival.size();
        int target = 0;
        int maxService = 0;
        vector<int> ans;
        priority_queue<pii,vector<pii>,greater<pii>> pq;
        vector<int> count(k,0);
        set<int> wait;
        
        for(int i = 0; i < k; ++i){
            wait.insert(i);
        }        
        for(int i = 0; i < n; ++i){
            while(!pq.empty() && pq.top().first <= arrival[i]){
                wait.insert(pq.top().second);
                pq.pop();
            }
            int curr = i%k;
            if(wait.empty()) continue;
            auto it = wait.lower_bound(curr);
            if(it != wait.end()){
                target = *it;
            }else{
                target = *wait.begin();
            }
            count[target]++;
            wait.erase(target);
            pq.push(make_pair(arrival[i] + load[i],target));
            maxService = max(maxService,count[target]);
        }
        
        for(int i = 0; i < k; ++i){
            if(count[i] == maxService) ans.push_back(i);
        }
        
        return ans;
    }
};
// @lc code=end

