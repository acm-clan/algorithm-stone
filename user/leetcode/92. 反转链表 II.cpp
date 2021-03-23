/*
 * @lc app=leetcode.cn id=92 lang=cpp
 *
 * [92] 反转链表 II
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
    ListNode* reverseBetween(ListNode* head, int left, int right) {
        if(head==nullptr || head->next==nullptr) return head;

        ListNode* sentry=new ListNode(0,head);  //因为涉及到head节点变动，所以用哨兵简化判断
        int cnt = 0;
        ListNode* curr = sentry;
        while(cnt<left-1){
            cnt++;
            curr=curr->next;
        }

        ListNode*hh=curr;
        ListNode*pre = curr->next;
        curr=pre->next;
        int l = right-left;
        while(l--){
            ListNode* ne = curr->next;
            curr->next = pre;

            pre = curr;
            curr= ne;
        }

        hh->next->next = curr;
        hh->next = pre;
        return sentry->next;
    }
};
// @lc code=end