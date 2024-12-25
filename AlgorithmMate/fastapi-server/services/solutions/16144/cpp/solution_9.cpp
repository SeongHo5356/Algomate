#include <iostream>
#include <vector>

using namespace std;

int main(){
	int n; scanf("%d",&n);
	vector<int> start;
	vector<int> end;
	int lower=-999999; int lowerx=1;
	int upper=999999; int upperx=1;
	for(int i=0;i<n;i++){
		int x; scanf("%d",&x);
		if(i>0){
			if(x<start.back()){
				printf("fail"); return 0;
			}
		}
		start.push_back(x);
		end.push_back(x+1);
	}
	for(int i=1;i<n;i++){
		for(int j=0;j<i;j++){
			int x=start[i]-end[j];
			int y=end[i]-start[j];
			int z=i-j;
			//printf("%d < %db < %d\n",x,z,y);
			if(lower*z<x*lowerx){
				lower=x; lowerx=z;
				//printf("lower: %d / %d\n",x,z);
			}
			if(upper*z>y*upperx){
				upper=y; upperx=z;
				//printf("upper: %d / %d\n",y,z);
			}
		}
	}
	if(lower*upperx>upper*lowerx){
		printf("fail");	
	}else printf("pass");
	
	return 0;
}