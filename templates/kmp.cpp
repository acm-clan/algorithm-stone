#include <queue>
#include <map>
#include <iostream>
#include <stdlib.h>
#include <string.h>
#include <stack>
#include <unordered_set>
#include <string>
using namespace std;

std::vector<int> compute_prefix_function(std::string & p)
{
    int n = p.length();
    std::vector<int> next(n);

    next[0] = -1;
    int j = 0;
    int k = -1;

    while(j<n-1){
        if(k == -1 || p[k] == p[j]){
            k++;
            j++;
            next[j] = k;
        }else{
            k = next[k];
        }
    }
    
    return next;
}

void print(std::vector<int> v)
{
    for(auto i : v){
        printf("%d ",i);
    }
    printf("\n");
}

int kmp_matcher(std::string & t, std::string & p)
{
    int n = t.length();
    int m = p.length();
    auto pi = compute_prefix_function(p);

    int j = 0;
    int k = 0;

    while(k<m && j<n){
        if(k == -1 || t[j] == p[k]){
            k++;
            j++;
        }else{
            k = pi[k];
        }
    }
    if(k == m){
        return j-m;
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