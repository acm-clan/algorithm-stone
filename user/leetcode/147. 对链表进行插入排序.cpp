/*
 * @lc app=leetcode.cn id=147 lang=cpp
 *
 * [147] 对链表进行插入排序
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
    ListNode* insertionSortList(ListNode* head) {
        if(head==nullptr || head->next==nullptr) return head;

        ListNode*sentry=new ListNode(0,nullptr);    //哨兵结点，简化 头插入特判情况
        ListNode*waitSort=head;
        while(waitSort){
            ListNode*pre =sentry;
              while(pre->next && waitSort->val>=pre->next->val){
                    pre=pre->next;
                }
                ListNode*ne =waitSort->next;        //插入结点的操作顺序需要注意
                waitSort->next = pre->next;
                pre->next = waitSort;
                waitSort=ne;
        }
        return sentry->next;
    }
};
// @lc code=end