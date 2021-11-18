#include<bits/stdc++.h>
using namespace std;

int T;
int n,m; 
string a;

int main()
{
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d%d",&n,&m);
		cin>>a; 
		int x=0,y=0,xmax=0,xmin=0,ymax=0,ymin=0;
		for(int i=0;i<a.size();++i)
		{
			switch(a[i])
			{
				case 'L': --y; break;
				case 'R': ++y; break;
				case 'D': ++x; break;
				case 'U': --x; break;
			}
			if(max(xmax,x)-min(xmin,x)==n||max(ymax,y)-min(ymin,y)==m) break;
			xmax=max(xmax,x);
			xmin=min(xmin,x);
			ymax=max(ymax,y);
			ymin=min(ymin,y);
		}
		cout<<-xmin+1<<' '<<-ymin+1<<endl;
	}
	
	return 0;
}

