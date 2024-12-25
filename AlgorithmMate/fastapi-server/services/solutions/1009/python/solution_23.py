import sys
input = sys.stdin.readline

T = int(input())

res = []

for _ in range(T):
    a, b = map(int, input().split())
    last = pow(a, b, 10)
    if last == 0:
        last = 10
    res.append(last)

for x in res:
    print(x)
