#include<iostream>
using namespace std;

int n,t,a;

int main()
{
	
	scanf("%d%d",&n,&t);
	for(int i=1;i<=n;i++)
	{
		scanf("%d",&a);
		t-=(86400-a);
		if(t<=0)
		{	
			cout<<i;
			return 0;
		}
	}
	
	return 0;
}
