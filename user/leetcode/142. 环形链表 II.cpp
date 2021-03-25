/*
 * @lc app=leetcode.cn id=142 lang=cpp
 *
 * [142] 环形链表 II
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
    //公式推导 抓距离相等slow*2=fast
    ListNode *detectCycle(ListNode *head) {
        if(head==nullptr ||head->next==nullptr) return nullptr;

        ListNode*slow=head,*fast=head;
        while(fast){
            slow=slow->next;
            fast=fast->next;
            if(fast) fast=fast->next;
            if(slow==fast) {
                ListNode*curr=head;
                ListNode*inCycle=fast;
                while(curr!=inCycle){
                    curr=curr->next;
                    inCycle=inCycle->next;
                }
                return inCycle;
            }
        }
        return nullptr;
    }
};
// @lc code=end