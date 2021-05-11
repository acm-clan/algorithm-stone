#include <iostream>
#include <map>
#include <queue>
#include <stack>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <unordered_set>
using namespace std;

// 计算kmp前缀表，用于匹配失败后进行回退操作
std::vector<int> compute_prefix_function(std::string& p)
{
    int n = p.length();
    std::vector<int> prefix(n);

    prefix[0] = -1;
    int j = 0;
    int k = -1;

    while (j < n - 1) {
        if (k == -1 || p[k] == p[j]) {
            // 如果相同，则记录当前k的位置
            k++;
            j++;
            prefix[j] = k;
        } else {
            // 不同则回退
            k = prefix[k];
        }
    }

    return prefix;
}

int kmp_matcher(std::string& t, std::string& p)
{
    auto prefix = compute_prefix_function(p);

    int j = 0;
    int k = 0;

    while (j < t.length() && k < p.length()) {
        if (k == -1 || t[j] == p[k]) {
            // 相同则前进
            k++;
            j++;
        } else {
            // 不同则回退尝试
            k = prefix[k];
        }
    }

    if (k == p.length()) {
        return j - p.length();
    }
    return -1;
}

void print(std::vector<int> v)
{
    for (auto i : v) {
        printf("%d ", i);
    }
    printf("\n");
}

int main()
{
    std::string t = "ababcabaa";
    std::string p = "bca";
    int pos = kmp_matcher(t, p);
    printf("pos:%d\n", pos);
    return 0;
}