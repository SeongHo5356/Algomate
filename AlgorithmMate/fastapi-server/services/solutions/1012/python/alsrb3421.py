import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MAX = 50 + 10

dy = [1, -1, 0, 0]
dx = [0, 0, 1 , -1]

def dfs(y, x):
    graph[y][x] = False
    for idx in range(4):
        ny = y + dy[idx]
        nx = x + dx[idx]
        if graph[ny][nx]:
            dfs(ny, nx)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y + 1][x + 1] = True

    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if graph[i][j]:
                dfs(i, j)
                answer += 1
    print(answer)