
/*
 * @lc app=leetcode.cn id=876 lang=cpp
 *
 * [876] 链表的中间结点
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
    ListNode* middleNode(ListNode* head) {
        //if(head==nulptr || head->next==nullptr) return head;   去除特殊情况

        //两个指针都从哨兵开始，避免slow=head，fast=head->next初始化时就是nullptr
        ListNode*sentry=new ListNode(0,head);   
        ListNode*slow=sentry,*fast=sentry;

        while(fast!=nullptr){
            slow=slow->next;
            fast=fast->next;
            if(fast)    fast=fast->next;
        }
        return slow;
    }
};
// @lc code=end
