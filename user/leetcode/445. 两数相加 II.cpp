445. 两数相加 II
/*
 * @lc app=leetcode.cn id=445 lang=cpp
 *
 * [445] 两数相加 II
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
    int stk1[10005],stk2[10005],top1=-1,top2=-1;
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode*curr=l1;
        while(curr){
            stk1[++top1] = curr->val;
            curr=curr->next;
        }
        curr=l2;
        while(curr){
            stk2[++top2]=curr->val;
            curr=curr->next;
        }

        curr=nullptr;
        int x=0;
        while(top1!=-1 || top2!=-1||x!=0){
            if(top1!=-1){ x+=stk1[top1];top1--;}
            if(top2!=-1){x+=stk2[top2];top2--;}
            ListNode*pre =new ListNode(x%10);
            pre->next = curr;

            curr=pre;
            x/=10;
        }
        return curr;
    }
};
// @lc code=end