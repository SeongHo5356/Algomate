#include <cstdio>

char rbuf[1<<20];
char wbuf[1<<20];
int idx, ridx, widx;

inline int unitSize(long long n){
    int ret = 1;
    while(n >= 10){
        ret++;
        n /= 10;
    }
    return ret;
}

void bflush(){
    fwrite(wbuf, 1, widx, stdout);
    widx = 0;
}

inline void writeLong(long long n){
    int isz = unitSize(n);
    if(isz + widx + 1 >= (1<<20)) bflush();

    int next = widx + isz;
    while(isz--){
        wbuf[widx + isz] = n % 10 + '0';
        n /= 10;
    }
    widx = next;
    wbuf[widx++] = '\n';
}
inline char read(){
    if(idx == ridx){
        ridx = fread(rbuf, 1, 1<<20, stdin);
        if(!ridx) return 0;
        idx = 0;
    }
    return rbuf[idx++];
}

inline int readInt(){
    int sum = 0;
    char now = read();

    while(now <= 32) now = read();
    while(now >= 48) sum = sum * 10 + now - '0', now = read();

    return sum;
}

int main(void) {
    int T = readInt(), N, A[1000000], len;
    while (T--) {
        N = readInt();
        for (int i = 0; i < N; i++) A[i] = readInt();
        long long result = 0;
        len = 0;
        for (int i = N - 1; i >= 0; i--) {
            if (len < A[i]) len = A[i];
            else result += len - A[i];
        }
        writeLong(result);
    }
    bflush();
}