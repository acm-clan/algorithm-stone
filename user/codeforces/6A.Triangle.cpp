#include <bits/stdc++.h>
using namespace std;

int a[5];

int main()
{
	
	for(int i=1;i<=4;i++) cin>>a[i];
	sort(a+1,a+5);
	if(a[1]+a[2]>a[3]||a[2]+a[3]>a[4]) cout<<"TRIANGLE"<<endl;
	else if(a[1]+a[2]==a[3]||a[2]+a[3]==a[4]) cout<<"SEGMENT"<<endl;
	else cout<<"IMPOSSIBLE"<<endl;
	
	
	return 0;
} 
