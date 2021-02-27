#include<iostream>
#include<cstring>
using namespace std;
int main(){
	
	char s1[505]={0},s2[505]={0};
	int n1[505]={0},n2[505]={0},ans[505]={0};
	
    cin>>s1>>s2;
    
    int l1=strlen(s1);
    int l2=strlen(s2);
    
    for(int i=0;i<l1;i++)
	{
		n1[i]=s1[l1-i-1]-'0';
	}
	for(int i=0;i<l2;i++)
	{
		n2[i]=s2[l2-i-1]-'0';
	}
	
	int len=l1>l2?l1:l2;
	
	for(int i=0;i<len;i++)
	{
		ans[i]=ans[i]+n1[i]+n2[i];
		if(ans[i]>=10)
		{
			ans[i]=ans[i]%10;
			ans[i+1]++;
		}
	}
	
	bool flag=false;
	
	for(int i=len;i>=0;i--)
	{
		if(ans[i]!=0||i==0)
		{
			flag=true;
		}
		
		if(flag)
		{
			cout<<ans[i];
		}
	}
	
	
	
    return 0;
}
