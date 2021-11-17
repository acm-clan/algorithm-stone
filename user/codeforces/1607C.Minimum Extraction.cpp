#include<bits/stdc++.h>
using namespace std;

const long long inf=0x3f3f3f3f3f3f3f3f;
long long n,a[200001],sum=0,mx=-inf;

int main()
{
	
	long long t;
	scanf("%lld",&t);
	while(t--)
	{
		sum=0,mx=-inf;
		scanf("%lld",&n);
		for(long long i=1;i<=n;++i) scanf("%lld",&a[i]);
		sort(a+1,a+1+n);
		for(long long i=1;i<=n;++i)
		{
			a[i]-=sum;
			sum+=a[i];
			mx=max(a[i],mx);
		}
		printf("%lld\n",mx);
	}
	return 0;
}
