#include <bits/stdc++.h>
using namespace std;
typedef long long lint;
typedef long double llf;
typedef pair<int, int> pi;
const int mod = 1e9 + 7;
const int MAXN = 100005;

int n, w[105];

int main(){
	cin >> n;
	for(int i=0; i<n; i++) cin >> w[i];
	for(int i=0; i<256; i++){
		for(int j=1; j<=n; j++){
			int alphmin = -1e9, alphmax = 1e9;
			for(int k=0; k<n; k++){
				alphmin = max(alphmin, w[k] * j - i * k);
				alphmax = min(alphmax, w[k] * j - i * k + j);
			}
			if(alphmin < alphmax){
				puts("pass");
				return 0;
			}
		}
	}puts("fail");
}
