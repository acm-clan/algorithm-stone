/*
 * @lc app=leetcode.cn id=109 lang=cpp
 *
 * [109] 有序链表转换二叉搜索树
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
//  不需要断链 只需要给出区间[head,tail)
    TreeNode* split(ListNode*head,ListNode*tail){
        if(head==tail) return nullptr;

        ListNode*slow=head,*fast=head;
        while(fast->next!=tail && fast->next->next!=tail){
            slow=slow->next;
            fast=fast->next->next;
        }
        TreeNode *root = new TreeNode(slow->val);
        root->left = split(head,slow);
        root->right = split(slow->next,tail);
        return root;
    }

    TreeNode* sortedListToBST(ListNode* head) {
        return split(head,nullptr);
    }
};
// @lc code=end