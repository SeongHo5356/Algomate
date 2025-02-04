#include <stdio.h>
#include <stdlib.h>

int main() {

	int N; scanf("%d", &N);

	float* PTRarray = (float*)malloc((sizeof(float) * N));
	//for (int i = 0; i < N; i += 1) scanf("%f", PTRarray + i);

	float interval[2]; float* PTRinterval = interval;

	float a, b;
	for (int n = 1; n <= N; n += 1) {

		scanf("%f", PTRarray + n-1);

		if (n == 1) continue;
		if (n == 2) {
			*(PTRinterval + 0) = ((*(PTRarray + 1) - (*(PTRarray + 0) + 1)) / (2 - 1)) * (3 - 1) + *(PTRarray + 0) + 1;
			*(PTRinterval + 1) = (((*(PTRarray + 1) + 1) - *(PTRarray + 0)) / (2 - 1)) * (3 - 1) + *(PTRarray + 0);
			//printf("seq:%d : get interval : (%f,%f)", n, *(PTRinterval + 0), *(PTRinterval + 1));
			continue;
		}

		a = *(PTRinterval + 0); if (a < *(PTRarray + n - 1)) a = *(PTRarray + n - 1);
		b = *(PTRinterval + 1); if (b > *(PTRarray + n - 1) + 1) b = *(PTRarray + n - 1) + 1;
		if (a >= b) { printf("fail"); return 0; }
		//printf("seq:%d : get intersection (%f,%f)\n", n, a, b);

		*(PTRinterval + 0) = ((a - (*(PTRarray + 0) + 1)) / (n - 1)) * (n)+*(PTRarray + 0) + 1;
		*(PTRinterval + 1) = ((b - *(PTRarray + 0)) / (n - 1)) * (n)+*(PTRarray + 0);
		if (*(PTRinterval + 0) < *(PTRarray + n - 1)) *(PTRinterval + 0) = *(PTRarray + n - 1);
		//printf("seq:%d : get interval : (%f,%f)", n, *(PTRinterval + 0), *(PTRinterval + 1));
	}

	printf("pass");

}