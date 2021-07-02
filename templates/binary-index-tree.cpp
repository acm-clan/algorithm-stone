#include <stdio.h>
#include <vector>
#include <stdlib.h>
#include <string.h>

class BinaryIndexedTree {
public:
    int n;
    std::vector<int> tree;

    int Lowbit(int x)
    {
        return x & -x;
    }

    int Query(int x)
    {
        int ans = 0;
        for (int i = x; i > 0; i -= Lowbit(i)) {
            ans += tree[i];
        }
        return ans;
    }

    void Add(int x, int u)
    {
        for (int i = x; i <= n; i += Lowbit(i)) {
            tree[i] += u;
        }
    }

    std::vector<int> vec;

    BinaryIndexedTree(std::vector<int>& nums)
    {
        n = nums.size();
        vec.assign(nums.begin(), nums.end());
        // tree = new int[n + 1]();
        tree.resize(n+1);
        for (int i = 0; i < n; ++i) {
            Add(i + 1, vec[i]);
        }
    }

    void UpdateValue(int index, int val)
    {
        Add(index + 1, val - vec[index]);
        vec[index] = val;
    }

    int SumRange(int left, int right)
    {
        return Query(right + 1) - Query(left);
    }
};

void test_perf(){
    int n = 100000;
    std::vector<int> v(n);

    for(int i=0; i<n; i++){
        v[i] = rand()%n;
    }

    for(int k=0; k<1000; k++){
        BinaryIndexedTree b(v);
        for(int i=0; i<10000; i++){
            int q = rand()%(n);
            int x = b.Query(q);
        }
        v.push_back(k);
    }
}

void test(){
    int n = 100;
    std::vector<int> v(n);

    for(int i=0; i<n; i++){
        v[i] = i+1;
    }

    BinaryIndexedTree b(v);
    for(int i=0; i<100; i++){
        int q = i+1;
        int x = b.Query(q);
        printf("query %d %d\n", q, x);

        x = b.SumRange(q, q+1);
        printf("sum %d %d\n", q, x);
    }
}

int main()
{
    test();
    return 0;
}
