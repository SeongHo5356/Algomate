import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(i, j):
    if not (0 <= i < N and 0 <= j < M):
        return
    if not G[i][j]:
        return
    G[i][j] = False
    dfs(i - 1, j)
    dfs(i + 1, j)
    dfs(i, j - 1)
    dfs(i, j + 1)

T = int(input())
for i in range(T):
    M, N, K = map(int, input().split())
    G = [[False] * M for i in range(N)]
    for i in range(K):
        x, y = map(int, input().split())
        G[y][x] = True
    S = 0
    for i in range(N):
        for j in range(M):
            if G[i][j]:
                S += 1
                dfs(i, j)
    print(S)