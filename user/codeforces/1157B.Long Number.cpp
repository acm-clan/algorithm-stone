#include <bits/stdc++.h>
using namespace std;

int n,a[200005],b[10];

int main()
{
	
	cin>>n;
	for(int i=1;i<=n;i++) scanf("%1d",&a[i]);
	for(int i=1;i<=9;i++) scanf("%d",&b[i]);
	for(int i=1;i<=n;i++)
	{
		if(a[i]<b[a[i]])
		{
			for(int j=i;a[j]<=b[a[j]]&&j<=n;j++)  a[j]=b[a[j]];
			break;
		}
	}
	for(int i=1;i<=n;i++) cout<<a[i];
	
	return 0;
}
