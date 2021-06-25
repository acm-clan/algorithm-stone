/*
 * @lc app=leetcode.cn id=752 lang=cpp
 *
 * [752] 打开转盘锁
 */

// @lc code=start
class Solution {
public:
    int string2int(string& s) {
        int res = 0;
        for(auto& c : s) {
            res *= 10;
            res += c - '0';
        }
        return res;
    }
    int openLock(vector<string>& deadends, string target) {
        if(target == "0000") return 0;
        int dp[10000];
        memset(dp,0,sizeof dp);
        // dp[i] = -1 为死亡数字
        // dp[i] = 1 为 "0000" 开始往后得到的数字
        // dp[i] = 2 为 target 开始往后得到的数字
        for(auto& i : deadends) dp[string2int(i)] = -1;
        if(dp[0] == -1) return -1;
        queue<string> q1;// "0000" 开始
        queue<string> q2;// target 开始
        int res = 0;
        q1.push("0000");
        q2.push(target);
        dp[0] = 1;
        dp[string2int(target)] = 2;
        while(!q1.empty() && !q2.empty()) {
            res ++;
            int len = q1.size();
            while(len --) {
                string t = q1.front();
                q1.pop();
                for(int i = 0;i < 4;i++) {
                    int x = t[i] - '0';
                    string t1 = t;
                    t1[i] = '0' +  ((x + 1) % 10);
                    int n = string2int(t1);
                    if(dp[n] == 2) {
                        return res;
                    } else if(dp[n] == 0) {
                        dp[n] = 1;
                        q1.push(t1);
                    } 

                    t1[i] = '0' +  ((x + 9) % 10);
                    n = string2int(t1);
                    if(dp[n] == 2) {
                        return res;
                    }
                    else if(dp[n] == 0) {
                        dp[n] = 1;
                        q1.push(t1);
                    }
                    //t[i] = '0' + x;
                }
            }
            res++;
            len = q2.size();
            while(len --) {
                string t = q2.front();
                q2.pop();
                for(int i = 0;i < 4;i++) {
                    int x = t[i] - '0';
                    string t1 = t;
                    t1[i] = '0' +  ((x + 1) % 10);
                    int n = string2int(t1);
                    if(dp[n] == 1) return res;
                    else if(dp[n] == 0) {
                        dp[n] = 2;
                        q2.push(t1);
                    } 

                    t1[i] = '0' +  ((x + 9) % 10);
                    n = string2int(t1);
                    if(dp[n] == 1) return res;
                    else if(dp[n] == 0) {
                        dp[n] = 2;
                        q2.push(t1);
                    } 
                    //t[i] = '0' + x;
                }
            }
        }
        return -1;
    }
};
// @lc code=end

