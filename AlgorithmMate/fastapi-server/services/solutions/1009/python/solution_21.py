import sys
T = int(sys.stdin.readline().strip())

for i in range(T):
    a, b = map(int, sys.stdin.readline().strip().split())
    com = pow(a, b, 10)
    if com == 0:
        com = 10
    print(com)