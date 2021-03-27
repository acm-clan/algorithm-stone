/*
 * @lc app=leetcode.cn id=148 lang=cpp
 *
 * [148] 排序链表
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
    //链表的归并排序
    //划分左右两部分
    //分别对两部分递归调用归并排序
    //合并有序的左右两部分
    ListNode* sortList(ListNode* head) {
        if(head==nullptr || head->next==nullptr) return head;

        ListNode*sentry=new ListNode(0,head),*fast=sentry,*slow=sentry;
        while(fast->next){
            slow=slow->next;
            fast=fast->next;
            if(fast->next) fast=fast->next;
        }//fast停留在最后一个结点，slow停留在奇数个中间，偶数的中间偏左 「n/2」
        ListNode*right = sortList(slow->next);
        slow->next=nullptr; //断链
        ListNode*left = sortList(sentry->next);

        //合并  
        ListNode*curr=sentry;
        while(left && right){
            if(left->val<right->val){
                curr->next =left;
                left = left->next;
            }else{
                curr->next=right;
                right=right->next;
            }
            curr=curr->next;
        }
        if(left) {curr->next =left;}
        if(right) {curr->next=right;}
        return sentry->next;
    }
};
// @lc code=end