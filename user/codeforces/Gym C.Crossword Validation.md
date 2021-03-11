**C.Crossword Validation**

题意:你被给予了一个完整的N * N的字谜棋盘。每个格子要么是一个小写字母，要么是一个'#'。同时，你被给予了一个M个不同单词的字典。棋盘中一个水平的候选单词是一行中完整且连续的单词直到不能扩展。就是说每一行都要找到最长的不能扩展的单词，直到遇到'#'，或者遇到边界。同时从上往下也要找到垂直的单词。然后要判断这些候选单词是否在M个不同单词的字典中出现，这个字典中每个单词都有一个分数，统计总和。同时判断是否存在这个候选单词，如果不存在，输出-1，否则输出总分数。

输入:输入第一行是一个T，表示测试数据的个数。

对于每一个测试数据，给出两个整数$N，M(1 <= N <= 1000, 1 <= M <= 4 * 10^{6})$，棋盘的大小和字典中单词的个数。接下来N行，每行是一个长度N的字符串，每个字符要么是小写字母，要么是'#'。接下来M行包含一个非空的字符串和一个分数，分数是正数。

题目保证所有测试数据的的$N^2$不会超过$4*10^{6}$。

做法:裸的字典树，首先把矩阵中的每个单词分割出来，从左到右，从上到下，具体的分割方式可以见代码，然后存到vector里面。之后再查询M个单词是否在字典树里面，统计分数。注意，如果分割出来aaaaa，我们查询aa，虽然在字典树中遍历到一个实际存在的节点，我们也要返回-1，我们可以判断它的分数score[p]是否等于-1即可。

```cpp
#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;
typedef long long ll;
const int N = 1005;
const int M = 4000005;
char s[N][N];
char s2[N], s3[N];

int son[M][26], idx;
int score[M];

void insert(char s[], int Score)
{
    int p = 0;
    for (int i = 0; s[i]; ++i)
    {
        int u = s[i] - 'a';
        if (!son[p][u]) son[p][u] = ++idx;
        p = son[p][u];
    }
    score[p] += Score;
}

int query(string& s)
{
    //cout << s << endl;
    int p = 0;
    for (int i = 0; i < s.size(); ++i)
    {
        int u = s[i] - 'a';
        if (!son[p][u]) return -1;
        p = son[p][u];
    }
    //注意这里，少了这句话就不行
    if (!score[p]) return -1;
    return score[p];
}

int main()
{
    int t;
    scanf("%d", &t);

    while (t--)
    {
        int n, m;
        scanf("%d%d", &n, &m);

        //预处理出字符串
        vector<string> v;

        for (int i = 1; i <= n; ++i) scanf("%s", s[i] + 1);
		//分割字符串的具体过程
        for (int i = 1; i <= n; ++i)
        {
            int len = 0;
            int len2 = 0;
            for (int j = 1; j <= n; ++j)
            {
                if (s[i][j] == '#')
                {
                    if (len)
                    {
                        s2[++len] = '\0';
                        v.push_back(s2 + 1);
                        len = 0;
                    }
                }
                else s2[++len] = s[i][j];
                if (s[j][i] == '#')
                {
                    if (len2)
                    {
                        s3[++len2] = '\0';
                        v.push_back(s3 + 1);
                        len2 = 0;
                    }
                }
                else s3[++len2] = s[j][i];
            }
            if (len)
            {
                s2[++len] = '\0';
                v.push_back(s2 + 1);
                len = 0;
            }
            if (len2)
            {
                s3[++len2] = '\0';
                v.push_back(s3 + 1);
                len2 = 0;
            }
        }

        int Score;
        for (int i = 1; i <= m; ++i)
        {
            scanf("%s%d", s2, &Score);
            insert(s2, Score);
        }

        bool flag = true;
        ll res = 0;
        //查询字典中的字符串，输出-1
        for (int i = 0; i < v.size(); ++i)
        {
            int score = query(v[i]);
            if (score == -1) flag = false;
            res += score;
        }

        if (!flag) printf("%d\n", -1);
        else printf("%lld\n", res);

        for (int i = 0; i <= idx; ++i)
        {
            memset(son[i], 0, sizeof son[i]);
            score[i] = 0;
        }
        idx = 0;
    }

    return 0;
}
```





