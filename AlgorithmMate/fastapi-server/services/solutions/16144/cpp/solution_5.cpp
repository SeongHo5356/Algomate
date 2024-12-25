#include <bits/stdc++.h>
using namespace std;
const double eps=1e-9;
int v[101],n;
double f(double a){
	double lb=0,ub=10000;
	for(int i=1;i<=n;i++){
		lb=max(lb,(double)(v[i]-a)/i);
		ub=min(ub,(double)(v[i]+1-a)/i);
	}
	return ub-lb;
}
int main(){
	scanf("%d",&n);
	for(int i=1;i<=n;i++)scanf("%d",v+i);
	double low=-1000,high=1000;
	for(int tt=0;tt<1000;tt++){
		double left=(low+low+high)/3;
		double right=(low+high+high)/3;
		double fl=f(left),fr=f(right);
		if(fl<fr)low=left;
		else high=right;
	}
	double a=(low+high)/2;
	if(f(a)<eps)puts("fail");
	else puts("pass");
}