// @before-stub-for-debug-begin
#include <vector>
#include <string>
#include "commoncppproblem720.h"

using namespace std;
// @before-stub-for-debug-end

/*
 * @lc app=leetcode.cn id=720 lang=cpp
 *
 * [720] 词典中最长的单词
 */
#include <vector>
#include <map>
#include <string>
using namespace std;

// @lc code=start
const int N = 1005, L = 30, CH = 26, mul = 131;
namespace Hash
{
	typedef unsigned int uint;
	const uint S = 12, S1 = 32 - S, M = 1996090921;
	struct node
	{
		int x, t;
	} h[(1 << S) + 1005];
	int T = 1;
	inline void insert(int x)
	{
		node *p = h + ((uint)x * M >> S1);
		for (; p->t == T; ++p)
			if (p->x == x)
				return;
		p->t = T;
		p->x = x;
	}
	inline bool find(int x)
	{
		for (node *p = h + ((uint)x * M >> S1); p->t == T; ++p)
			if (p->x == x)
				return 1;
		return 0;
	}
}
using namespace Hash;

vector<int> v[L + 1];
inline uint gethash(char *s, int l)
{
	uint res = 0;
	for (char *end = s + l; s != end; ++s)
		res = res * mul + *s;
	return res;
}
class Solution
{
public:
	string longestWord(vector<string> &w)
	{
		string *ans = new string();
		for (int i = 1; i <= L; ++i)
			v[i].clear();
		for (int i = 0; i < w.size(); ++i)
			v[w[i].size()].push_back(i);
		++T;
		insert(0);
		for (int i = 1; i <= L; ++i)
		{
			for (int j = 0; j < v[i].size(); ++j)
			{
				string &str = w[v[i][j]];
				uint t = gethash(&str[0], i - 1);
				if (find(t))
				{
					insert(t * mul + str[i - 1]);
					if (ans->size() < i || *ans > str)
						ans = &str;
				}
			}
			if (ans->size() < i)
				break;
		}
		return *ans;
	}
};

//IO
int _IO = []()
{
	ios::sync_with_stdio(0);
	cin.tie(0); //cout.tie(0);
	return 0;
}();
// @lc code=end
