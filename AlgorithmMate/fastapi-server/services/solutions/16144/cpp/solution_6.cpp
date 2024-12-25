#include <cstdio>
#include <iostream>
#include <cassert>
#include <queue>
#include <deque>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <set>
#include <cstdlib>
#include <string>
#include <unordered_map>
#include <map>
#include <sstream>
#include <bitset>
#include <random>
#include <tuple>
#include <array>
#include <tgmath.h>
#include <functional>
using namespace std;

//#define VERBOSE

typedef long long int lli;
typedef pair<int, int> pii;
typedef unsigned char byte;
typedef unsigned int uint;
typedef unsigned long long int ulli;

int b[120];

typedef struct _frac {
    int a, b;
    _frac(int x, int y) {
        a = x;
        b = y;
    }
} frac;

bool operator<(frac a, frac b) {
    return (lli)a.a * b.b < (lli)a.b * b.a;
}

int main() {
    int n;
    scanf("%d", &n);
    int i, j;
    frac mn = frac(0, 1), mx = frac(10000, 1);
    for (i=0; i<n; ++i) {
        scanf("%d", b+i);
        for (j=0; j<i; ++j) {
            if (b[j] > b[i]) return!~puts("fail");
            mn = max(mn, frac(b[i] - b[j] - 1, i - j));
            mx = min(mx, frac(b[i] - b[j] + 1, i - j));
        }
    }
    puts(mx < mn ? "fail" : "pass");
}