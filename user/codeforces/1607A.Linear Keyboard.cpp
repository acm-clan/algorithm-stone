#include<bits/stdc++.h>
using namespace std;

int t;
long long x,n,res;

int main() 
{#include<bits/stdc++.h>
using namespace std;

int t;
int alphabeta[30];
char a;
string s;
int ans=0;

inline int read()
{
    int x=0,f=1;
    char ch=getchar();
    while(ch<'0'||ch>'9')
	{
        if(ch=='-') f=-1;
        ch=getchar();
    }
    while(ch>='0'&&ch<='9')
	{
        x=x*10+(ch-'0');
        ch=getchar();
    }
    return x*f;
}

int main()
{
	
	t=read();
	for(int i=1;i<=t;i++)
	{
		memset(alphabeta,-1,sizeof(alphabeta));
		ans=0;
		
		for(int j=1;j<=26;j++)
		{
			cin>>a;
			alphabeta[a-'a'+1]=j;
		}
		cin>>s;
		for(int j=0;j<s.length()-1;j++)
		{
			ans+=abs(alphabeta[s[j+1]-'a'+1]-alphabeta[s[j]-'a'+1]);
		}
		printf("%d\n",ans);
	}
	
	
	return 0;
}
	cin>>t;
	while(t--) 
	{
		cin>>x>>n;
		res=x;
		for(long long i=n/4*4+1;i<=n;i++) 
		{
			if(res%2) res+=i;
			else res-=i;
		}
		cout<<res<<endl;
	}
	
	return 0;
}
