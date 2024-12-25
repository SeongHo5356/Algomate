#include <stdio.h>
#include <algorithm>
using namespace std;
int arr[100];
int main(void)
{
    int n; scanf("%d",&n);
    double s,e,ss,ee;
    for(int i=0;i<n;i++)
        scanf("%d",arr+i);
    s = (double)(arr[1] - (arr[0]+1)); e = (double)(arr[1]+1 - arr[0]); //s<x<e
    for(int i=2;i<n;i++)
    {
        for(int j=0;j<i;j++)
        {
            ss = ((double)arr[i] - (arr[j]+1))/(double)(i-j);
            ee = ((double)(arr[i]+1) - (arr[j]))/(double)(i-j);
            //printf("%.10lf ~ %.10lf\n",ss,ee);
            s = max(ss,s); e = min(ee,e);
        }
    }
    //printf("%.10lf %.10lf\n",s,e);
    if(e<=0||s>=e)
        printf("fail\n");
    else
        printf("pass\n");
}