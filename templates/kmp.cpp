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
    int m = p.length();
    std::vector<int> next(m);

    next[0] = -1;
    int i = 0;
    int j = -1;

    while(i<m){
        if(j == -1 || p[i] == p[j]){
            i++;
            j++;
            next[i] = j;
        }else{
            j = next[j];
        }
    }

    for(auto i : next){
        printf("%d ", i);
    }
    printf("\n");
    
    return next;
}

int kmp_matcher(std::string & t, std::string & p)
{
    int n = t.length();
    int m = p.length();
    printf("n %d m %d\n", n, m);
    auto pi = compute_prefix_function(p);
    // int q = 0;
    // for(int i=0; i<n;){
    //     while(q>0 && p[q+1]!=t[i]){
    //         q = pi[q];
    //     }
    //     if(pi[q+1] == t[i]){
    //         q++;
    //     }
    //     if(q == m){
    //         return i-m;
    //     }
    // }
    return 0;
}

int main()
{
    std::string t = "ababcabaa";
    std::string p = "ababcabaa";
    int pos = kmp_matcher(t, p);
    printf("pos:%d\n", pos);
    return 0;
}