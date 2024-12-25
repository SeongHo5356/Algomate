import sys
input = sys.stdin.readline

cached = ["10", "1", "2486", "3971", "46", "5", "6", "7931", "8426", "91"]

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    s = cached[a % 10]
    print(s[b % len(s) - 1] if a % 10 > 0 else s)