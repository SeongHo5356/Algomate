#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
 
int main() {
    int T;
    
    cin >> T;
    while(T--) {
        int N;
        long long int num;
        long long int big = -1;
        long long int sum = 0;
        vector<int> v;
        
        cin >> N;
        while(N--) {
            cin >> num;
            v.push_back(num);
        }
        
        reverse(v.begin(), v.end()); //뒤에서부터 비교하기 위함
        
        for(int i = 0; i < v.size(); i++) {
            if(big < v[i]) {
                big = v[i];
            }
            else {
                sum += big - v[i];
            }
        }
        
        cout << sum << '\n';
        
    }
    return 0;
}