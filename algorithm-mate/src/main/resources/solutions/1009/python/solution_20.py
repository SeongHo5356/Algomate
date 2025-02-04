import sys

for i in range(int(sys.stdin.readline().rstrip())):
    a, b = map(int, sys.stdin.readline().split())
    c = pow(a, b, 10)
    if(c != 0):
        print(c)
    else:
        print(10)