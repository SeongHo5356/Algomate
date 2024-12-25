import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a, b = map(int, input().split())
    num = b%4 if b%4 else 4
    ans = (a**num)%10
    print(ans if ans else 10)