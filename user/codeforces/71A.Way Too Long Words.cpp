#include<bits/stdc++.h>
using namespace std;
int main()
{
	
    int n;
	string a;
	int i;
	cin>>n;
	for(i=0;i<n;i++)
	{
		 cin>>a;
	 	 if(a.length()>10)
	     {
	 	      cout<<a[0]<<a.length()-2<<a[a.length()-1]<<endl;
		 }
		 else
		 {
		 	cout<<a<<endl;
		 }
	} 
	
	return 0;
}
