#include<bits/stdc++.h>
using namespace std;
int N;
typedef long long ll;
typedef double ld;
vector<int>V;
struct A
{
    ll B,E;
    A(ll b,ll e):B(b),E(e){}
    void merge(A Tt)
    {
        B=max(B,Tt.B);
        E=min(E,Tt.E);
    }
};
tuple<int,double> low(ld XX)
{
    double TD=V[0]-XX;
    int ID=0;
    for(int i=1;i<V.size();i++)
    {
        if(TD<=(V[i]-XX)/(i+1))
        {
            TD=(V[i]-XX)/(i+1);
            ID=i;
        }
    }
    return tie(ID,TD);
}
tuple<int,double> upp(ld XX)
{
    double TD=V[0]-XX+1;
    int ID=0;
    for(int i=1;i<V.size();i++)
    {
        if(TD>(V[i]-XX+1)/(i+1))
        {
            TD=(V[i]-XX+1)/(i+1);
            ID=i;
        }
    }
    return tie(ID,TD);
}
int main()
{
    cin>>N;
    V.resize(N);
    for(auto&I:V)cin>>I;
    A RNG(-1000,1000);
    for(int i=0;i<V.size()-1;i++)
        RNG.merge(A((i+2)*V[i]-(i+1)*V[i+1]-(i+1),(i+2)*V[i]-(i+1)*V[i+1]+i+2));
    if(RNG.E<=RNG.B)
    {
        puts("fail");
        return 0;
    }
    ld l=RNG.B,r=RNG.E,m;
    int cnt=100;while(--cnt)
    {
        m=(l+r)/2;
        tuple<int,double> lo=low(m),up=upp(m);
        if(get<1>(lo)>=get<1>(up))
        {
            if(get<0>(lo)<get<0>(up))l=m;
            else r=m;
        }
        else
        {
            if(get<1>(up)>0)
                puts("pass");
            else puts("fail");
            return 0;
        }
    }
    puts("fail");
}
