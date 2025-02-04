import sys
input = sys.stdin.readline
sys.setrecursionlimit(5000)

def dfs(x, y):
    graph[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1:
                dfs(nx, ny)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

case = int(input())
for i in range(case):
    M,N,T = map(int,input().split())
    graph = [[0]*(M) for i in range(N)]
    for i in range(T):
        a,b = map(int,input().split())
        graph[b][a] = 1
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                dfs(i,j)
                cnt +=1

    print(cnt)