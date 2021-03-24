/*
 * @lc app=leetcode.cn id=295 lang=cpp
 *
 * [295] 数据流的中位数
 */

// @lc code=start
class MedianFinder {
public:
    /** initialize your data structure here. */
    priority_queue<int, vector<int>, greater<int>> small; //升序
    priority_queue<int, vector<int>, less<int>> big; //降序
    MedianFinder()
    {
    }

    void addNum(int num)
    {
        if (small.empty() && big.empty()) {
            small.push(num);
            return;
        }

        if (num >= small.top())
            small.push(num);

        else
            big.push(num);

        if (big.size() > small.size() + 1) {
            int a = big.top();
            small.push(a);
            big.pop();
        }

        else if (small.size() > big.size() + 1) {
            int b = small.top();
            big.push(b);
            small.pop();
        }
    }

    double findMedian()
    {
        if (big.size() == small.size())
            return (big.top() + small.top()) * 0.5;
        else if (big.size() > small.size())
            return big.top();
        else
            return small.top();
    }
};

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder* obj = new MedianFinder();
 * obj->addNum(num);
 * double param_2 = obj->findMedian();
 */
// @lc code=end
