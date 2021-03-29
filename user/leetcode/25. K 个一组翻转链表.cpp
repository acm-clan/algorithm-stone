/*
 * @lc app=leetcode.cn id=25 lang=cpp
 *
 * [25] K 个一组翻转链表
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
    ListNode* recursion(ListNode*head,int len,int cut){
        if(len<cut||cut==1) return head;

        ListNode*sentry=new ListNode(0,head),*pre=nullptr,*curr=head,*ne=nullptr;
        int k=cut;
        while(k--){
            ne=curr->next;
            curr->next = pre;

            pre = curr;
            curr= ne;
        }
        //sentry->next就是最初的head 需要连接上后面反转好的部分
        sentry->next->next = recursion(ne,len-cut,cut);
        return pre;
    }
    ListNode* reverseKGroup(ListNode* head, int k) {
        int l=0;
        for(auto i=head;i!=nullptr;i=i->next){
            l++;
        }
        return recursion(head,l,k);
    }
};
// @lc code=end