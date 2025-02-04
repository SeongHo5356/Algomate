#include<bits/stdc++.h>
//#define double long double
//T.erase(unique(T.begin(),T.end()),T.end());
//written by djs100201
#define all(v) v.begin(),v.end()
using namespace std;
using ll = long long;
using P = pair<ll, ll>;
using PP = pair<ll, P>;
const ll n_ = 2020 + 100, inf = (ll)2e9 * (ll)1e9 + 7, mod = 1e9 + 7, sqrtN = 320;
ll dy[8] = { -1,0,1,0,1,-1,-1,1 }, dx[8] = { 0,1,0,-1,1,1,-1,-1 };
ll n, m, k, tc = 1, a, b, c, sum, x, y, z, base, ans, q;
ll gcd(ll x, ll y) {
	if (!y)return x;
	return gcd(y, x % y);
}
void solve() {
	cin >> n;
	vector<ll>v(n + 1);
	for (int i = 1; i <= n; i++)cin >> v[i];
	long double a = 0, b = 1e9;
	for (int i = 2; i <= n; i++) {
		if (v[i] < v[i - 1]) {
			cout << "fail";
			return;
		}
		//a = max(a, v[i] - (v[i - 1] + 1)), b = min(b, v[i] + 1 - v[i - 1]);
	}
	for (int i = 1; i <= n; i++)
		for (int j = i + 1; j <= n; j++) {
			a = max(a, (v[j] - (v[i] + 1)) / (long double)(j - i));
			b = min(b, (v[j] + 1 - v[i]) / (long double)(j - i));
		}
	if (a < b)cout << "pass";
	else cout << "fail";
	//a< k <b

}
int main() {
	ios_base::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);
	//cin >> tc;
	while (tc--)solve();
}