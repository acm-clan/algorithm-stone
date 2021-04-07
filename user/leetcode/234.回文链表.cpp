/*
 * @lc app=leetcode.cn id=234 lang=cpp
 *
 * [234] 回文链表
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
    //前半部分 和 后半部分的值相等
    //反转后半部分（使用栈） 得到前半部分
    bool isPalindrome(ListNode* head) {
        if(head==nullptr ||head->next==nullptr) return true;

        ListNode*slow=head,*fast=head->next;
        while(fast->next){
            slow=slow->next;
            fast=fast->next;
            if(fast->next) fast=fast->next;
        }
        ListNode*right = slow->next;
        slow->next =nullptr;

        ListNode*pre=nullptr,*curr=right,*ne=nullptr;
        while(curr){
            ne = curr->next;
            curr->next = pre;

            pre = curr;
            curr = ne;
        }
        right = pre;
        ListNode*left = head;
        while(right){
            if(right->val != left->val) return false;
            right=right->next;
            left=left->next;
        }
        return true;
    }
};
// @lc code=end