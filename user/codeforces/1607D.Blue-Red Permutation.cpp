#include<bits/stdc++.h>
using namespace std;

int T;
int n,a[200005];
char s[200005];

bool cmp(int x,int y)
{
	return x>y;
}

int main()
{
	
	scanf("%d",&T);
	begin:
	while(T--)
	{
		vector<int> blue,red;
		scanf("%d",&n);
		for(int i=1;i<=n;i++) 
		{
			scanf("%d",&a[i]);
		}
		cin>>s+1;
		for(int i=1;i<=n;i++) 
		{
			if(s[i]=='B') blue.push_back(a[i]);
			else red.push_back(a[i]);
		}
		sort(blue.begin(),blue.end());
		sort(red.begin(),red.end(),cmp);
		for(int i=0;i<red.size();i++)
		{
			if(red[i]>n-i) 
			{
				cout<<"NO"<<endl;
				goto begin;
			}
		}
		for(int i=0;i<blue.size();i++)
		{
			if(blue[i]<i+1) 
			{
				cout<<"NO"<<endl;
				goto begin;
			}
		}
		cout<<"YES"<<endl;
	}
	
	
	
	return 0;
}
