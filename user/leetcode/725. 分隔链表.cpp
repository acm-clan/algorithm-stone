
/*
 * @lc app=leetcode.cn id=725 lang=cpp
 *
 * [725] 分隔链表
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
    vector<ListNode*> splitListToParts(ListNode* root, int k) {
        vector<ListNode*>res(k,nullptr);
        if(root==nullptr) return res;

        int l=0;
        for(ListNode*i=root;i!=nullptr;i=i->next){
            l++;
        }
        int avgLen=l/k,remains=l%k;

        ListNode*curr=root,*prev=nullptr;
        for(int i=0;i<k;i++){
            ListNode* subHead=curr;
            int len = avgLen;
            if(remains){len+=1;remains--;}
            while(len--){
                prev = curr;
                curr = curr->next;
            }
            prev->next=nullptr;
            res[i] = subHead;
        }

        return res;
    }
};
// @lc code=end
