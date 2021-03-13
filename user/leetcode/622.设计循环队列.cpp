/*
 * @lc app=leetcode.cn id=622 lang=cpp
 *
 * [622] 设计循环队列
 */

#include <queue>
using namespace std;

// @lc code=start
class MyCircularQueue {
public:
    queue<int> q;
    int cap = 0;
    MyCircularQueue(int k) {
        cap = k;
    }
    
    bool enQueue(int value) {
        if(q.size()>=cap){
            return false;
        }
        q.push(value);
        return true;
    }
    
    bool deQueue() {
        if(q.empty()){
            return false;
        }
        q.pop();
        return true;
    }
    
    int Front() {
        if(q.empty()){
            return -1;
        }
        return q.front();
    }
    
    int Rear() {
        if(q.empty()){
            return -1;
        }
        return q.back();
    }
    
    bool isEmpty() {
        return q.empty();
    }
    
    bool isFull() {
        return q.size()==cap;
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */
// @lc code=end

