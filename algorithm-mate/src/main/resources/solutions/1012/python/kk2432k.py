import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def d(x,y):
    if x<0 or x>=M or y<0 or y>=N:pass
    elif lst[y][x]:
        lst[y][x]=0
        d(x-1,y)
        d(x+1,y)
        d(x,y-1)
        d(x,y+1)
    else:pass


for _ in range(int(input())):
    M,N,K=map(int,input().split())
    lst=[[0]*M for _ in range(N)]
    result=0

    for i in range(K):
        X,Y=map(int,input().split())
        lst[Y][X]=1

    for y in range(N):
        for x in range(M):
            if lst[y][x]:                
                d(x,y)
                result+=1

    print(result)