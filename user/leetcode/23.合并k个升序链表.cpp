/*
 * @lc app=leetcode.cn id=23 lang=cpp
 *
 * [23] 合并K个升序链表
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
    struct cmp{
        bool operator()(ListNode*a,ListNode*b){
            return a->val >b->val;
        }
    };
    priority_queue<ListNode*,vector<ListNode*>,cmp >pq;
    unordered_map<ListNode*,int>node2index;
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        ListNode*sentry=new ListNode();
        if(lists.size()==0)  return nullptr;
        
        for(int i=0;i<lists.size();i++){
            if(lists[i]){
                pq.push(lists[i]);
                node2index[lists[i]]=i;
                lists[i] = lists[i]->next;
            }
        }

        ListNode*curr=sentry;
        while(!pq.empty()){
            ListNode*tmp=pq.top();
            pq.pop();
            curr->next =tmp;
            curr=curr->next;
            int i = node2index[tmp];
            if(lists[i])  {
                pq.push(lists[i]);
                node2index[lists[i]]=i;
                lists[i]=lists[i]->next;
            }
        }
        curr->next=nullptr;
        ListNode*res=sentry->next;
        delete sentry;
        return res;
    }
};
// @lc code=end

