/*
 * @lc app=leetcode.cn id=1019 lang=cpp
 *
 * [1019] 链表中的下一个更大节点
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
    int stk[10005],top=-1;
    vector<int> nextLargerNodes(ListNode* head) {
         vector<int>vals;
         for(auto i=head;i!=nullptr;i=i->next){
             vals.push_back(i->val);
         }
         vector<int>res(vals.size(),0);

        int l =vals.size();
        for(int i=0;i<l;i++){
            while(top!=-1&& vals[stk[top]] < vals[i]){
                res[stk[top]] = vals[i];
                top--;
            }
            stk[++top] = i;
        }
        return res;
    }
};
// @lc code=end
