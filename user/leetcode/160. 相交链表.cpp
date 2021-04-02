/*
 * @lc app=leetcode.cn id=160 lang=cpp
 *
 * [160] 相交链表
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
 // 构造一段路程，使得两个指针相遇的时候走过的路程相等 空间O(1) 时间O(N)
 // 使用一个set记录 空间O（n） 时间O（N）
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        //if(headA==nullptr || headB==nullptr) return nullptr;

        ListNode*a=headA,*b=headB;
        while(a!=b){
            if(a!=nullptr) a=a->next;
            else a=headB;

            if(b!=nullptr) b=b->next;
            else b=headA;
        }
        return a;
    }
};
// @lc code=end
