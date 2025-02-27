#include <stdio.h>  
#include <algorithm>  
#include <assert.h>
#include <bitset>
#include <cmath>  
#include <complex>  
#include <deque>  
#include <functional>  
#include <iostream>  
#include <limits.h>  
#include <map>  
#include <math.h>  
#include <queue>  
#include <set>  
#include <stdlib.h>  
#include <string.h>  
#include <string>  
#include <time.h>  
//#include <unordered_map>  
#include <unordered_set>  
#include <vector>
#pragma warning(disable:4996)
#pragma comment(linker, "/STACK:336777216")
using namespace std;
#define mp make_pair
#define Fi first
#define Se second
#define pb(x) push_back(x)
#define szz(x) ((int)(x).size())
#define rep(i, n) for(int i=0;i<n;i++)
#define all(x) (x).begin(), (x).end()
#define ldb ldouble  
typedef tuple<int, int, int> t3;
typedef long long ll;
typedef unsigned long long ull;
typedef double db;
typedef long double ldb;
typedef pair <int, int> pii;
typedef pair <ll, ll> pll;
typedef pair <ll, int> pli;
typedef pair <db, db> pdd;
int IT_MAX = 1 << 17;
const ll MOD = 5000011;
const int INF = 0x3f3f3f3f;
const ll LL_INF = 0x3f3f3f3f3f3f3f3f;
const db PI = acos(-1);
const db ERR = 1e-10;

int in[105];
int main() {
	int N, i, j, k;
	scanf("%d", &N);
	for (i = 1; i <= N; i++) scanf("%d", &in[i]);
	for (i = 1; i < N; i++) if (in[i] > in[i + 1]) return !printf("fail\n");

	for (i = 1; i <= 105; i++) {
		for (j = 1; j <= 26000; j++) {
			ll st = in[1] * i, en = (in[1] + 1) * i - 1;
			for (k = 2; k <= N; k++) {
				ll s = in[k] * i - j * (k - 1);
				ll e = (in[k] + 1) * i - j * (k - 1) - 1;
				st = max(st, s), en = min(en, e);
				if (st > en) break;
			}
			if (st <= en) return !printf("pass\n");
		}
	}
	return !printf("fail\n");
}