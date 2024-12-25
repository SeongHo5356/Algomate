import sys

input = sys.stdin.readline

T = int(input())

def dfs(r, c):
    stack = [(r, c)]
    visited[r][c] = True

    while stack:
        sr, sc = stack.pop()
        for dr, dc in dir:
            nr, nc = sr + dr, sc + dc
            if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and field[nr][nc] == 1:
                visited[nr][nc] = True
                stack.append((nr, nc))

for tc in range(T):
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    dir = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    worm = 0

    for _ in range(K):
        x, y = map(int, input().split())
        field[y][x] = 1

    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]:
                dfs(i, j)
                worm += 1

    print(worm)
