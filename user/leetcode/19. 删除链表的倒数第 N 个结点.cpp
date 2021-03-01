/*
 * @lc app=leetcode.cn id=19 lang=cpp
 *
 * [19] 删除链表的倒数第 N 个结点
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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode*sentry = new ListNode(0,head);
        ListNode* fast=head,*slow=sentry;
        for(int i=0;i<n;i++){
            fast = fast->next;
        }   //此时快慢指针相差n+1

        while(fast!=nullptr){
            fast=fast->next;
            slow=slow->next;
        }// fast理解成倒数第0个，则slow倒数第n+1个,slow->next为倒数第n个
        slow->next =slow->next->next;
        ListNode*ans=sentry->next;
        delete sentry;
        return ans;

    }
};
// @lc code=end