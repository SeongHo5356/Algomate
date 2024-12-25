import sys
input = sys.stdin.readline

t = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    stack = [(x,y)]
    visited[x][y] = True

    while stack:
        x,y = stack.pop()

        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not  visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                stack.append((nx,ny))

for _ in range(t):
    m,n,k = map(int,input().split())
    arr = [[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
   
    for _ in range(k):
        y,x = map(int,input().split())
        arr[x][y] = 1

    cnt = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1 and not visited[i][j]:
                dfs(i,j)
                cnt += 1
    
    print(cnt)