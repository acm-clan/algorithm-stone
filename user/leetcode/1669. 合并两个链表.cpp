/*
 * @lc app=leetcode.cn id=1669 lang=cpp
 *
 * [1669] 合并两个链表
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
    ListNode* mergeInBetween(ListNode* list1, int a, int b, ListNode* list2) {
        ListNode *curr=list1;

        //先找到左右需要修改的节点
        int cnt=0;
        while(cnt!=a-1){
            cnt++;
            curr=curr->next;
        }
        ListNode* left=curr;
        
        while(cnt!=b){
            cnt++;
            curr=curr->next;
        }
        ListNode* right=curr->next;
        
        //再找到list2的头尾节点
        ListNode *last=list2;
        while(last->next){
            last=last->next;
        }
        left->next = list2;
        last->next = right;
        return list1;
    }
};
// @lc code=end