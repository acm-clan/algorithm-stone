#include<bits/stdc++.h>
using namespace std;

long long a,b,c;
long long x,y;

int kzo(int a,int b)
{
	if(b==0)
	{
		x=1;
		y=0;
		return a;
	}
	long long tmp=kzo(b,a%b);
	long long t=x;
	x=y;
	y=(t-a/b*y);
	return tmp;
}

int main()
{
	
	scanf("%lld%lld%lld",&a,&b,&c);
	c=-c;
	long long d=kzo(a,b);
	if(c%d!=0)
	{
		printf("-1\n");
		return 0;
	}
	x=c/d*x,y=c/d*y;
	printf("%lld %lld\n",x,y);
	
	return 0;
}
