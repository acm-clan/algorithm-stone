#include<bits/stdc++.h>
using namespace std;

int n,k;

int main()
{
	
	cin>>n>>k; 
	for(int x=1;x<=n;x++)
	{
		if(x*(x+1)*2.5+k>240)
		{
			cout<<x-1;
			return 0;
		}
	}

	cout<<n;
	
	
	return 0;
}
