#include <bits/stdc++.h>
#define sz(x) ((int)x.size())
#define all(x) (x).begin(), (x).end()
using namespace std;
typedef long long ll;
typedef long double ld;
const int scale = 1000000;
int n, a[110];
int main() {
	scanf("%d", &n);
	for(int i=0; i<n; i++) {
		scanf("%d", a+i); a[i] *= scale;
		if(i>0 && a[i-1] > a[i]) { puts("fail"); return 0; }
	}
	if(n==1) { puts("pass"); return 0; }
	for(int i=0; i<scale; i++) {
		pair<ll,ll> mx={1,-1e9}, mn={1,1e9};
		for(int j=1; j<n; j++) {
			if(1ll*mx.second*(scale*j) < 1ll*(a[j]-a[0]-i)*mx.first)
				mx = {scale*j, a[j]-a[0]-i};
			if(1ll*mn.second*(scale*j) > 1ll*(a[j]+scale-a[0]-i)*mn.first)
				mn = {scale*j, a[j]+scale-a[0]-i};
		}
		if(1ll*mx.second*mn.first<1ll*mn.second*mx.first) {
			puts("pass");
			return 0;
		}
	}
	puts("fail");
	return 0;
}