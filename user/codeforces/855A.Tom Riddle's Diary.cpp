#include<bits/stdc++.h>
using namespace std;

map<string,bool>k;
int n;
string a;

int main()
{
	
	cin>>n;
	for(int i=1;i<=n;i++)
	{
		cin>>a;
		k[a]?cout<<"YES\n":cout<<"NO\n";
		k[a]=1;//因为map的初始值为空，所以可以直接判断
	}
	
	
	return 0;
}
