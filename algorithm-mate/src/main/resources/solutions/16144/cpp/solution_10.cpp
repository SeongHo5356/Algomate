#include <iostream>
#define MAXN 102

using namespace std;

bool good_line(int n, int beta[MAXN], int x0, int dx, int dy){
    for(int x = 0; x < n; ++x){
        if(x < x0){
            int y = beta[x0] - (dy * (x0 - x) + dx - 1) / dx;
            if(y != beta[x]){
                return false;
            }
        }else if(x > x0){
            int y = beta[x0] + (dy * (x - x0) - 1) / dx;
            if(y != beta[x]){
                return false;
            }
        }
    }
    return true;
}

bool any_good_line(int n, int beta[MAXN]){
    for(int i = 0; i < n; ++i){
        for(int j = i + 1; j < n; ++j){
            int dx = j - i, dy = beta[j] + 1 - beta[i];
            if(dy > 0 && good_line(n, beta, i, dx, dy)){
                return true;
            }
        }
    }
    return false;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    int beta[MAXN];
    for(int i = 0; i < n; ++i){
        cin >> beta[i];
    }
    if(any_good_line(n, beta)){
        cout << "pass\n";
    }else{
        cout << "fail\n";
    }
    return 0;
}