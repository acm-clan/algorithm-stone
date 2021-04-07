/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
    Node* flatten(Node* head) {
        //if(head==nullptr) return head;

        Node*curr=head;
        while(curr){
            if(curr->child){
                Node*childlast=curr->child;
                while(childlast->next!=nullptr) childlast=childlast->next;

                curr->child->prev=curr;
                childlast->next=curr->next;
                if(curr->next) curr->next->prev=childlast;
                curr->next = curr->child;
                curr->child=nullptr;
            }
            curr=curr->next;
        }
        return head;
    }
};