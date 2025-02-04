import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    if a % 10 == 0:
        print(10)
    else:
        print(pow(a, b, 10))