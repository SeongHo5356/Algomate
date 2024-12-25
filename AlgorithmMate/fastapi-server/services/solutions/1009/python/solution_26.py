import sys
n = int(input())

def mod(n, m):
    n %= m
    if n==0:
        return m
    return n

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if ((a%10)**mod(b, 4))%10:
        print(((a%10)**mod(b, 4))%10)
    else:
        print(10)