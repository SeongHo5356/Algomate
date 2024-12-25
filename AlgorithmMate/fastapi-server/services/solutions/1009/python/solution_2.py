import sys

T = int(sys.stdin.readline().rstrip())

for i in range(T):
    a,b=map(int, sys.stdin.readline().rstrip().split())
    mid=b%4
    if mid == 0:
        fin=a**4
    else:
        fin=a**mid

    result=fin%10
    
    if result==0:
        print(10)
    else:
        print(fin%10)