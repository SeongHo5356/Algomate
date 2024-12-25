#include <iostream>
#include <bits/stdc++.h>

#include <algorithm>
#include <string>
#include <cstring>
#include <memory>
#include <cmath>

//data structure
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <utility>
#include <set>
#include <list>
#include <tuple>

#define INF 1e9+1
#define MAX
#define X first
#define Y second
#define MOD 1000000007

using namespace std;

typedef pair <int, int> pii;
typedef long long ll;
typedef unsigned long long ull;
typedef pair <ll, ll> pll;

//--------struct,class-area



//---------variable-area

int A[101];

//---------function-area


//---------end

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(NULL); cout.tie(NULL);

//----------start

    int N; cin >> N;
    for (int i = 1; i <= N; i++)
        cin >> A[i];

    double m = 0, M = 1e9;
    for (int i = 1; i <= N; i++)
        for (int j = i+1; j <= N; j++) {
            m = max(m, double(A[j]-A[i]-1) / double(j-i));
            M = min(M, double(A[j]-A[i]+1) / double(j-i));
        }

    if (m < M)
        cout << "pass";
    else
        cout << "fail";


//-----------end

    return 0;
}


