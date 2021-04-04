/*
 * @lc app=leetcode.cn id=817 lang=cpp
 *
 * [817] 链表组件
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    // 唯一值，链表的值是否在G中，使用set判断
    int numComponents(ListNode* head, vector<int>& G) {
        unordered_set<int>nums(G.begin(),G.end());
        int cnt=0;
        ListNode*curr=head;
        while(curr){
            if(nums.count(curr->val)){
                cnt+=1;
                while(curr &&nums.count(curr->val)){curr=curr->next;}
            }else{curr=curr->next;}
        }
        return cnt;
    }
};
// @lc code=end