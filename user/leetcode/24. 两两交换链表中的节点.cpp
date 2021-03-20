/*
 * @lc app=leetcode.cn id=24 lang=cpp
 *
 * [24] 两两交换链表中的节点
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
    ListNode* swapPairs(ListNode* head) {
        if(head==nullptr ||head->next ==nullptr) return head;
        ListNode*sentry=new ListNode(0,head);
        ListNode*pre=sentry,*curr=sentry->next;

        //建议画图理解，重点在于pre 和 curr的选取，交换A和B，一定要知道A前面一个结点
        while(curr && curr->next){
            pre->next = curr->next;
            curr->next = pre->next->next;
            pre->next->next=curr;

            pre = curr;
            curr=curr->next;
        }
        return sentry->next;   //可能修改head指针指向，所以不能return head
    }
};

class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        if(head==nullptr || head->next==nullptr) return head;

        ListNode* ne = head->next;
        head->next = swapPairs(ne->next);
        ne->next = head;
        return ne;
    }
};
// @lc code=end