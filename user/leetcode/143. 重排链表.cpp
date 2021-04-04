/*
 * @lc app=leetcode.cn id=143 lang=cpp
 *
 * [143] 重排链表
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
    //前半部分不变，后半部分反转插入 考察寻找中间结点+断链反转后插入
    void reorderList(ListNode* head) {
        if(head==nullptr || head->next==nullptr) return;
        ListNode*slow=head,*fast=head->next;

        while(fast->next){
            slow=slow->next;
            fast=fast->next;
            if(fast->next) fast=fast->next;
        }
        ListNode *reverse = slow->next,*pre=nullptr;
        slow->next=nullptr; //注意：断链！！
        while(reverse){
            ListNode*ne = reverse->next;
            reverse->next =pre;

            pre=reverse;
            reverse=ne;
        }

        slow = head;
        fast = pre;
        while(fast){
            ListNode*ne = fast->next;
            fast->next = slow->next;
            slow->next =fast;

            slow = fast->next;
            fast = ne;
        }
    }
};
// @lc code=end
