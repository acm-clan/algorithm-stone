/*
 * @lc app=leetcode.cn id=2 lang=cpp
 *
 * [2] 两数相加
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* sentry=new ListNode(0,l1);
        ListNode* curr = sentry;
        int temp=0;
        while(l1 || l2){    //一直加 直到l1和l2都为空
            if(l1) {temp+=l1->val;l1=l1->next;}
            if(l2) {temp+=l2->val;l2=l2->next;}
            curr->next = new ListNode(temp%10,nullptr);
            curr=curr->next;
            temp =temp/10;
        }
        if(temp) curr->next=new ListNode(temp,nullptr);
        return sentry->next;
    }
};
// @lc code=end