import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**8)

dx,dy=[0,0,-1,1],[-1,1,0,0]
def dfs(x,y):
    arr[x][y]=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<n and 0<=ny<m and arr[nx][ny]==1:
            dfs(nx,ny)

t=int(input())
for _ in range(t):
    m,n,k=map(int, input().split())
    arr=[[0]*(m) for _ in range(n)]
    for _ in range(k):
        x,y=map(int, input().split())
        arr[y][x]+=1

    cnt=0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                dfs(i,j)
                cnt+=1
    print(cnt)