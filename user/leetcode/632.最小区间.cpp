/*
 * @lc app=leetcode.cn id=632 lang=cpp
 *
 * [632] 最小区间
 */

// @lc code=start
/***************************************************
Author: hqztrue
https://github.com/hqztrue/LeetCodeSolutions
Complexity: O(sort(n))
If you find this solution helpful, plz give a star:)
***************************************************/
const int N=175005,M=3500,U=100000;
struct node{
	int t,id;
}v[N];
void radix_sort(node A[],int l,int r){  //a[i]>=0
	const int base=511,W=9,T=2;
	static node B[N];
	static int s[base+1];
	A+=l-1;r-=l-1;l=1;
	node *a=A,*b=B; int x=0;
	for (int i1=1;i1<=T;++i1){
		for (int i=0;i<=base;++i)s[i]=0;
		for (int i=1;i<=r;++i)++s[a[i].t>>x&base];
		for (int i=1;i<=base;++i)s[i]+=s[i-1];
		for (int i=r;i>=1;--i)b[s[a[i].t>>x&base]--]=a[i];
		swap(a,b); x+=W;
	}
	if (a!=A)for (int i=1;i<=r;++i)A[i]=a[i];
}
int s[M];
class Solution {
public:
	vector<int> smallestRange(vector<vector<int>>& nums) {
		int n=nums.size(),v1=0,res=~0u>>1; vector<int> ans(2);
		for (int i=0;i<n;++i)
			for (auto &x:nums[i]){v[v1].t=x+U; v[v1++].id=i;}
		radix_sort(v,0,v1-1);
		for (int i=0;i<n;++i)s[i]=0;
		for (int l=0,r=-1,cnt=0;;){
			while (cnt<n){
				++r; if (r==v1)break;
				int &s0=s[v[r].id]; cnt+=!s0; ++s0;
			}
			if (r==v1)break;
			while (cnt==n){
				if (v[r].t-v[l].t<res)res=v[r].t-v[l].t,ans[0]=v[l].t,ans[1]=v[r].t;
				int &s0=s[v[l].id]; --s0; cnt-=!s0; ++l;
			}
		}
		ans[0]-=U; ans[1]-=U;
		return ans;
	}
};

//IO
int _IO=[](){
	ios::sync_with_stdio(0);
	cin.tie(0); //cout.tie(0);
	return 0;
}();

// @lc code=end

