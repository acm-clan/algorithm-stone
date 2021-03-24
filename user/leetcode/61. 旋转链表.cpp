/*
 * @lc app=leetcode.cn id=61 lang=cpp
 *
 * [61] 旋转链表
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

    ListNode* rotateRight(ListNode* head, int k) {
        if(head==nullptr || head->next ==nullptr) return head;//不管有用没用，先处理特殊情况更稳妥
        int l=0;
        for(auto i=head;i!=nullptr;i=i->next){l++;}
        k=k%l;

        ListNode*sentry=new ListNode(0,head);
        ListNode*slow=sentry,*fast=sentry;
        while(k--){
            fast=fast->next;
        }

        while(fast->next !=nullptr){
            slow=slow->next;
            fast=fast->next;
        }
        fast->next = head;
        head =slow->next;
        slow->next=nullptr;
        return head;
    }
};
// @lc code=end