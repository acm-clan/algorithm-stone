/*
 * @lc app=leetcode.cn id=86 lang=cpp
 *
 * [86] 分隔链表
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
    ListNode* partition(ListNode* head, int x) {
        if(head==nullptr || head->next==nullptr) return head;

        ListNode* sentry1=new ListNode(0,nullptr),* smaller=sentry1;
        ListNode* sentry2=new ListNode(0,nullptr),* larger=sentry2;
        ListNode*curr=head;
        while(curr){
            if(curr->val<x) {
                smaller->next = curr;
                smaller = smaller->next;
            }else{
                larger->next=curr;
                larger=larger->next;
            }
            curr=curr->next;
        }
        smaller->next = sentry2->next;
        larger->next=nullptr; //记得末尾要指向空！！
        return sentry1->next;
    }
};
// @lc code=end