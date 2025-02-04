import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6)

dx = [1,-1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    global visited
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if graph[nx][ny] and not visited[nx][ny]:
            dfs(nx,ny)

t = int(input())

for _ in range(t):
    M,N,K = map(int,input().split())
    graph = [[False] * (N+2) for _ in range(M+2)]
    visited = [[False] * (N+2) for _ in range(M+2)]
    for _ in range(K):
        x,y = map(int,input().split())
        graph[x+1][y+1] = True

    answer = 0
    for i in range(1,M+1):
        for j in range(1,N+1):
            if not visited[i][j] and graph[i][j]:
                dfs(i,j)
                answer += 1
    print(answer)





