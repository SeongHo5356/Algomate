#include <cstdio>
#include <algorithm>
#include <utility>

using namespace std;

int n;
double arr[101];

double get(double val) {
	double mx=-1e15,mn=1e15;
	for(int i=1;i<=n;i++) {
		mx=max(mx,arr[i]+1-i*val);
		mn=min(mn,arr[i]+1-i*val);
	}
	return mx-mn;
}
int main() {
	scanf("%d",&n);
	for(int i=1;i<=n;i++) scanf("%lf",arr+i);

	double lo=0,up=1e9;
	for(int i=0;i<100;i++) {
		double m1=(lo*2+up)/3, m2=(lo+up*2)/3;
		double v1=get(m1),v2=get(m2);
		if(v1 < v2) up=m2;
		else lo=m1;
	}
	if(get(lo)<1.0) puts("pass");
	else puts("fail");

	return 0;
}