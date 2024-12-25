import sys
input=sys.stdin.readline
t=int(input())

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    queue=[(x,y)]
    graph[x][y]=0
    while queue:
        x,y=queue.pop(0)
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or nx>=m or ny<0 or ny>=n:
                continue
            if graph[nx][ny]==1:
                queue.append((nx,ny))
                graph[nx][ny]=0

for i in range(t):
    m,n,k=map(int,input().split())
    graph=[ [0] * n for _ in range(m)]
    cnt=0
    for i in range(k):
        x,y=map(int,input().split())
        graph[x][y]=1
    for a in range(m):
        for b in range(n):
            if graph[a][b]==1:
                bfs(a,b)
                cnt+=1
    print(cnt)
