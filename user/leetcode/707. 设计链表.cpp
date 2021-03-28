/*
 * @lc app=leetcode.cn id=707 lang=cpp
 *
 * [707] 设计链表
 */

// @lc code=start
class MyLinkedList {
public:
    /** Initialize your data structure here. */
    struct Node{
        int val;
        Node *next;
        Node(int val,Node*ne):val(val),next(ne){}
    };
    Node *sentry;
    int l;

    MyLinkedList() {
        sentry=new Node(0,nullptr);
        l=0;
    }
    
    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    int get(int index) {
        if(index<0 || index>=l) return -1;

        Node*curr=sentry->next;
        for(int i=0;i<index;i++){
            curr=curr->next;
        }
        return  curr->val;
    }
    
    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    void addAtHead(int val) {
        sentry->next = new Node(val,sentry->next);
        l+=1;
    }
    
    /** Append a node of value val to the last element of the linked list. */
    void addAtTail(int val) {
        Node *curr=sentry;
        while(curr->next){
            curr=curr->next;
        }
        curr->next = new Node(val,nullptr);
        l+=1;
    }
    
    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    void addAtIndex(int index, int val) {
        Node*curr = sentry;
        if(index<=0){
            addAtHead(val);
        }else if(index<=l){
            l+=1;
            for(int i=0;i<index;i++){
                curr=curr->next;
            }
            Node*tmp=new Node(val,curr->next);
            curr->next = tmp;
        }

    }
    
    /** Delete the index-th node in the linked list, if the index is valid. */
    void deleteAtIndex(int index) {
        if(index<0 || index>=l) return;

        l-=1;
        Node*curr=sentry;
        for(int i=0;i<index;i++){
            curr=curr->next;
        }
        curr->next = curr->next->next;
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */
// @lc code=end