import sys
input = sys.stdin.readline

t = int(input())
for i in range(0, t):
    inputs = list(map(int, input().split()))
    a = inputs[0]
    b = inputs[1]
    result = pow(a, b, 10)
    if result == 0: result = 10
    print(result)
