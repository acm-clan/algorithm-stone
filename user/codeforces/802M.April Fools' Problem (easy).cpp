#include<bits/stdc++.h>
using namespace std;

int n,k;
int num=0;
int a[3005];

int main()
{
	
	cin>>n>>k;
	for(int i=1;i<=n;i++)
	{
		cin>>a[i];
	}
	sort(a+1,a+1+n);
	for(int i=1;i<=k;i++)
	{
		num+=a[i];
	}
	cout<<num;
	
	
	return 0;
}
