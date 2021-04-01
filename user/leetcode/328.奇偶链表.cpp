/*
 * @lc app=leetcode.cn id=328 lang=cpp
 *
 * [328] 奇偶链表
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
    ListNode* oddEvenList(ListNode* head) {
        if(head==nullptr || head->next==nullptr) return head;

        ListNode* odd=new ListNode(0),*last=odd;
        ListNode* even=new ListNode(1),*end=even;
        ListNode*curr=head;
        int flag=1;
        while(curr){
            if(flag){
                last->next = curr;
                last=last->next;
            }else{
                end->next = curr;
                end=end->next;
            }
            flag= flag^1;
            curr=curr->next;
        }

        last->next = even->next;
        end->next =nullptr;
        return odd->next;
    }
};
// @lc code=end
