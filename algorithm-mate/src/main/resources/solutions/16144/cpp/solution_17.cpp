#include <bits/stdc++.h>
#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <vector>
#include <assert.h>
#include <map>
#include <set>
#include <stdlib.h>
#include <math.h>
#include <string>
#include <time.h>
#include <string.h>
#include <queue>
#include <complex>
#include <iomanip>
#include <stack>
using namespace std;
typedef long long int ll;
typedef unsigned long long int ull;
typedef complex<double> base;
ll mod=1e9+7;
double eps=1e-9;
ll exp(ll x,ll y){if(y<0) return 0; ll ret=1;for(;y;y>>=1,x=(x*x)%mod){if(y&1)ret=(ret*x)%mod;}return ret;}
ll pexp(ll x, ll y){if(y<0) return 0; ll ret=1; for(;y;y>>=1,x=(x*x)){if(y&1)ret=(ret*x);}return ret;}
ll gcd(ll x,ll y){if(!x||!y) return x+y; return x%y==0?y:gcd(y,x%y);}
ll lcm(ll x,ll y){return x*(y/gcd(x,y));}
ll bsum(ll u,ll b){ll ret=0;if(u<b)return u;while(u){ret+=u%b;u/=b;}return ret;}
ll prival(ll u,ll p){ll cn=0;while(u%p==0){cn++;u=u/p;}return cn;}
ll minv(ll a,ll b){return 1<a?b-minv(b%a,a)*b/a:1;}
ll extm(ll a,ll b){ll ret=0;while(a!=0){if(a%2==1){ret+=b;ret%=mod;}a>>=1;b=(2*b)%mod;}return ret;}   
ll eaphi(ll x){ll t=x,ret=x,i;for(i=2;i*i<=x;i++){if(t%i==0){ret-=ret/i;while(t%i==0) t/=i;}}if(t!=1) ret-=ret/t;return ret;}
ll eadivc(ll x){ll ret=0;ll i;for(i=1;i*i<=x;i++){if(x%i==0 && i*i!=x) ret+=2;if(x%i==0 && i*i==x) ret+=1;}return ret;}
ll eadivs(ll x){ll ret=0;ll i;for(i=1;i*i<=x;i++){if(x%i==0 && i*i!=x) ret+=i+x/i;if(x%i==0 && i*i==x) ret+=i;}return ret;}
ll ndig(ll x, ll b){ll ret=0;while(x){x/=b; ret++;}return ret;}
ll rev(ll n, ll b){ll ret=0;while(n){ret=b*ret+n%b; n/=b;}return ret;}
ll sq(ll x){ll t=(ll)sqrt(x); for(ll i=t-2 ; i<=t+2 ; i++) if(i*i==x) return abs(i); return -1;}
ll extexp(ll x,ll y){if(y<0) return 0; ll ret=1;for(;y;y>>=1,x=extm(x,x)){if(y&1)ret=extm(ret,x);}return ret;}
bool isprime(ll x){if(x<=1) return false; for(ll i=2;i*i<=x;i++){if(x%i==0){return false;}}return true;}
bool pos=false;
ll n, num[111];

bool trial(int u, int v)
{
	ll p=num[v]-num[u]; ll q=v-u; if(p<0) return false;
	ll mxp=-1e8; ll mxq=1;
	ll mip=1e8; ll miq=1;	
	int i;
	for(i=1 ; i<=n ; i++)
	{
		if((num[i]*q-i*p)*mxq>mxp*q)
		{
			mxp=(num[i]*q-i*p); mxq=q;
			ll g=gcd(abs(mxp),abs(mxq));
			mxp/=g; mxq/=g;
		}
		if((num[i]*q-i*p)*miq<mip*q)
		{
			mip=(num[i]*q-i*p); miq=q;
			ll g=gcd(abs(mip),abs(miq));
			mip/=g; miq/=g;
		}
	}
	if(mxp*miq<mxq*mip+mxq*miq) return true;
	return false;
}

int main(void)
{
	cin>>n; int i, j;
	for(i=1 ; i<=n ; i++) cin>>num[i];
	for(i=1 ; i<=n ; i++)
	{
		for(j=i+1 ; j<=n ; j++)
		{
			pos=pos|trial(i,j);
		}
	}
	if(pos) printf("pass");
	else printf("fail");
	return 0;
}