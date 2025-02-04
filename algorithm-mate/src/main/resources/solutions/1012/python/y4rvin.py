import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def check(i,j):
    g[i][j]=2
    if i==0:
        if j==0:
            if g[i+1][j]==1:
                g[i+1][j]=2
                check(i+1,j)
            if g[i][j+1]==1:
                g[i][j+1]=2
                check(i,j+1)
        elif j==m-1:
            if g[i+1][j]==1:
                g[i+1][j]=2
                check(i+1,j)
            if g[i][j-1]==1:
                g[i][j-1]=2
                check(i,j-1)
        else:
            if g[i+1][j]==1:
                g[i+1][j]=2
                check(i+1,j)
            if g[i][j+1]==1:
                g[i][j+1]=2
                check(i,j+1)
            if g[i][j-1]==1:
                g[i][j-1]=2
                check(i,j-1)
    elif i==n-1:
        if j==0:
            if g[i-1][j]==1:
                g[i-1][j]=2
                check(i-1,j)
            if g[i][j+1]==1:
                g[i][j+1]=2
                check(i,j+1)
        elif j==m-1:
            if g[i-1][j]==1:
                g[i-1][j]=2
                check(i-1,j)
            if g[i][j-1]==1:
                g[i][j-1]=2
                check(i,j-1)
        else:
            if g[i-1][j]==1:
                g[i-1][j]=2
                check(i-1,j)
            if g[i][j+1]==1:
                g[i][j+1]=2
                check(i,j+1)
            if g[i][j-1]==1:
                g[i][j-1]=2
                check(i,j-1)
    else:
        if j==0:
            if g[i+1][j]==1:
                g[i+1][j]=2
                check(i+1,j)
            if g[i-1][j]==1:
                g[i-1][j]=2
                check(i-1,j)
            if g[i][j+1]==1:
                g[i][j+1]=2
                check(i,j+1)
        elif j==m-1:
            if g[i+1][j]==1:
                g[i+1][j]=2
                check(i+1,j)
            if g[i-1][j]==1:
                g[i-1][j]=2
                check(i-1,j)
            if g[i][j-1]==1:
                g[i][j-1]=2
                check(i,j-1)
        else:
            if g[i][j+1]==1:
                g[i][j+1]=2
                check(i,j+1)
            if g[i+1][j]==1:
                g[i+1][j]=2
                check(i+1,j)
            if g[i-1][j]==1:
                g[i-1][j]=2
                check(i-1,j)
            if g[i][j-1]==1:
                g[i][j-1]=2
                check(i,j-1)
    
for _ in range(int(input())):
    cnt = 0
    m,n,k = map(int, input().split())
    g = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(k):
        x,y = map(int,input().split())
        g[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if g[i][j]:
                if g[i][j]==1:
                    cnt += 1
                    check(i,j)
    print(cnt)