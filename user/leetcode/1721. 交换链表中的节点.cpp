/*
 * @lc app=leetcode.cn id=1721 lang=cpp
 *
 * [1721] 交换链表中的节点
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
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode *sentry=new ListNode(0,head);
        ListNode *lk=sentry;
        int i =0;
        while(i!=k){
            i++;
            lk=lk->next;
        }
        
        ListNode *tmp=lk;
        ListNode *rk=sentry;
        while(tmp!=nullptr){
            tmp=tmp->next;
            rk=rk->next;
        }

        int x = lk->val;
        lk->val = rk->val;
        rk->val = x;

        return head;
    }
};
// @lc code=end