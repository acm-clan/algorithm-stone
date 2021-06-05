/*
 * @lc app=leetcode.cn id=212 lang=cpp
 *
 * [212] 单词搜索 II
 */

// @lc code=start
constexpr int N = 7E3, M = 26;
int n, m, top, tree[N][M], parent[N];
bool isEnd[N], vis[14][14];
char buf[11];

void insert(string str) {
	for (char& c : str) c -= 'a';
	int rt = 1;
	for (int j = str.length() - 1; j >= 0; --j) {
		if (!tree[rt][str[j]]) {
			tree[rt][str[j]] = top++;
			parent[tree[rt][str[j]]] = rt;
		}
		rt = tree[rt][str[j]];
	}
	isEnd[rt] = 1;
}

class Solution {
	vector<vector<char>> board;
	vector<string> ans;

	void dfs(int rt, int x, int y, int len) {
		if (isEnd[rt]) {
			string temp(len, 'a');
			for (int j = len - 1; j >= 0; --j) temp[j] += buf[len - j - 1];
			ans.push_back(temp);
			isEnd[rt] = false;
			bool flag = false;
			for (int i = rt, j = len - 1; !flag && j >= 0; --j) {
				for (int k = 0; k < M; ++k) {
					if (!tree[i][k]) continue;
					flag = true; break;
				}
				if (!flag) tree[i = parent[i]][buf[j]] = 0;
			}
		}

		if (!vis[x + 1][y + 1] && tree[rt][board[x][y]]) {
			vis[x + 1][y + 1] = true;
			buf[len] = board[x][y];
			dfs(tree[rt][board[x][y]], x + 1, y, len + 1);
			dfs(tree[rt][board[x][y]], x - 1, y, len + 1);
			dfs(tree[rt][board[x][y]], x, y + 1, len + 1);
			dfs(tree[rt][board[x][y]], x, y - 1, len + 1);
			vis[x + 1][y + 1] = false;
		}
	}
public:
	vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
		for (auto& cv : board) for (char& c : cv) c -= 'a';

		this->board = board;
		m = board.size();
		n = board[0].size();

		memset(parent, 0, sizeof parent);
		memset(vis, 0, sizeof vis);
		memset(tree, 0, sizeof tree);
		memset(isEnd, 0, sizeof isEnd);
		::top = 2;

		for (int i = 0; i < m + 2; ++i) vis[i][0] = vis[i][n + 1] = true;
		for (int j = 0; j < n + 2; ++j) vis[0][j] = vis[m + 1][j] = true;

		for (string& s : words) insert(s);

		for (int i = 0; i < m; ++i) {
			for (int j = 0; j < n; ++j) {
				dfs(1, i, j, 0);
			}
		}

		return ans;
	}
};

int FAST_IO = []() {
	std::ios::sync_with_stdio(0);
	std::cin.tie(0);
	std::cout.tie(0);
	return 0;
}();
// @lc code=end

