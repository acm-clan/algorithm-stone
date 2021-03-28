/*
 * @lc app=leetcode.cn id=138 lang=cpp
 *
 * [138] 复制带随机指针的链表
 */

// @lc code=start
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    map<Node*,Node*>old2new;

    Node* copyRandomList(Node* head) {
        if(head==nullptr) return head;

        Node*sentry=new Node(0),*copyLast=sentry;
        Node*curr=head;
        while(curr){
            copyLast->next = new Node(curr->val);
            old2new.insert(make_pair(curr,copyLast->next));
            curr=curr->next;
            copyLast=copyLast->next;
        }

        curr=head;
        copyLast=sentry->next;
        while(curr){
            copyLast->random = old2new[curr->random];
            copyLast=copyLast->next;
            curr=curr->next;
        }
        return sentry->next;
    }
};
// @lc code=end