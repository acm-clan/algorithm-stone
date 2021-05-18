#include <iostream>
#include <map>
#include <queue>
#include <stack>
#include <stdlib.h>
#include <string.h>
#include <string>
#include <unordered_set>
using namespace std;

std::vector<int> compute_prefix_function(std::string& p)
{
    int n = p.length();
    std::vector<int> next(n);

    next[0] = -1;
    int j = 0;
    int k = -1;

    while (j < n - 1) {
        if (k == -1 || p[k] == p[j]) {
            k++;
            j++;
            next[j] = k;
        } else {
            k = next[k];
        }
    }

    return next;
}

void print(std::vector<int> v)
{
    for (auto i : v) {
        printf("%d ", i);
    }
    printf("\n");
}

int kmp_matcher(std::string& t, std::string& p)
{
    auto next = compute_prefix_function(p);

    int j = 0;
    int k = 0;

    while (j < t.length() && k < p.length()) {
        if (k == -1 || t[j] == p[k]) {
            k++;
            j++;
        } else {
            k = next[k];
        }
    }

    if (k == p.length()) {
        return j - p.length();
    }
    return -1;
}

int main()
{
    std::string t = "ababcabaa";
    std::string p = "bca";
    int pos = kmp_matcher(t, p);
    printf("pos:%d\n", pos);
    return 0;
}