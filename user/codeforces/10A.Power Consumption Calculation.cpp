#include<bits/stdc++.h>
using namespace std;

int n,p1,p2,p3,t1,t2;
int l,r,s,ans=0;
    
int main()
{
	scanf("%d%d%d%d%d%d",&n,&p1,&p2,&p3,&t1,&t2);
    for(int i=1;i<=n;i++)
    {
    	scanf("%d%d",&l,&r);
        if(i>1)
        {
            ans=ans+min(t1,l-s)*p1;
	        if(l-s>t1)
	        {
	            ans=ans+min(l-s-t1,t2)*p2;
	            if(l-s>t1+t2)
	            {
	                ans=ans+(l-s-t1-t2)*p3;
	            }
	        }		
        }		
        ans=ans+(r-l)*p1;
        s=r;	
    } 
    printf("%d",ans);
    
    return 0;
}
