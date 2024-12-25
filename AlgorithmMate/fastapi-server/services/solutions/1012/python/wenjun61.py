import sys
input=sys.stdin.readline
t=int(input())
dx=[-1,1,0,0]
dy=[0,0,-1,1]
def bfs(x,y):
    queue=[(x,y)]
    grid[x][y]= -1
    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if grid[nx][ny]==1:
                queue.append((nx,ny))
                grid[nx][ny]= -1

for i in range(t):
    m,n,k=map(int,input().split())
    grid=[[0 for _ in range(n)] for _ in range(m)]
    count = 0

    for _ in range(k):
        x,y=map(int,input().split())
        grid[x][y]=1
    for r in range(m):
        for c in range(n):
            if grid[r][c]==1:
                bfs(r,c)
                count += 1
    print(count)