import sys

input = sys.stdin.readline

for i in range(int(input())):
    a,b = map(int, input().split())
    r = [a ** i % 10 for i in range(1,5)][(b % 4) - 1]
    print(r if r != 0 else 10)