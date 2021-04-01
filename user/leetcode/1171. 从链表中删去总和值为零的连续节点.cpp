/*
 * @lc app=leetcode.cn id=1171 lang=cpp
 *
 * [1171] 从链表中删去总和值为零的连续节点
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
    //连续的序列和为0，实际上就存在一个区间和为0,立刻推出前缀和存在相等S[x] - S[y] = a[y+1] +...+ a[x] = 0 
    // 注意点 存在整个前缀和为0 所以需要哨兵结点 求S[全部]的前缀和  
    map<int,ListNode*>presum2node;
    ListNode* removeZeroSumSublists(ListNode* head) {
        ListNode*sentry=new ListNode(0,head);
        ListNode*curr=sentry;
        int S=0;
        while(curr){
            S+=curr->val;
           presum2node[S] = curr;   //前缀和最右侧的结点
           curr=curr->next;
        }

        curr=sentry;
        S=0;
        while(curr){
            S+=curr->val;
            curr->next = presum2node[S]->next;
            curr=curr->next;
        }
        return sentry->next;
    }
};
// @lc code=end