#include <cstdio>
using namespace std;

namespace FIO {
	const size_t BUFFER_SIZE = 524288;
	char buffer[BUFFER_SIZE];
	char* ptr = buffer + BUFFER_SIZE;

	inline char readByte() {
		if (ptr == buffer + BUFFER_SIZE) {
			fread(buffer, 1, BUFFER_SIZE, stdin);
			ptr = buffer;
		}
		return *(ptr++);
	}

	unsigned int readUnsigned() {
		unsigned int ret = 0;
		char c = readByte();
		while (!('0' <= c && c <= '9')) {
			c = readByte();
		}
		while ('0' <= c && c <= '9') {
			ret = ret * 10 + (c - '0');
			c = readByte();
		}
		return ret;
	}
};

int n;
int cost[1000000];

void proc() {
	n = FIO::readUnsigned();
	for (int i = 0; i < n; ++i) {
		cost[i] = FIO::readUnsigned();
	}

	long long ans = 0;
	int maxcost = 0;
	for (int i = n - 1; i >= 0; --i) {
		if (maxcost < cost[i]) {
			maxcost = cost[i];
		}
		else {
			ans += maxcost - cost[i];
		}
	}
	printf("%lld\n", ans);
}

int main() {
	//freopen("input.txt", "r", stdin);
	int t = FIO::readUnsigned();
	while (t-- > 0) {
		proc();
	}
	return 0;
}