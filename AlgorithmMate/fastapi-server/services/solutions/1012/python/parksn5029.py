import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(graph, x, y):
    graph[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0 <= nx < N and 0 <= ny < M:
            if graph[nx][ny] == 1:
                dfs(graph, nx, ny)

Q = int(input())

result = []
for _ in range(Q):
    N, M, K = map(int, input().split())
    graph = [[0]*M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
    
    cnt = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                dfs(graph, i, j)
                cnt +=1
    print(cnt)