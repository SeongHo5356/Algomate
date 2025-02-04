# 1012. 유기농 배추

import sys

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def dfs(y, x):
    visited[y][x] = 1

    while True:
        for a in range(4):
            move_x = x + dx[a]
            move_y = y + dy[a]

            if 0 <= move_x < M and 0 <= move_y < N and matrix[move_y][move_x] == 1 and visited[move_y][move_x] == 0:
                stack.append([y, x])
                visited[move_y][move_x] = 1
                x, y = move_x, move_y
                break

        else:
            if stack:
                y, x = stack.pop()
            else:
                break


T = int(sys.stdin.readline())

for tc in range(1, T + 1):
    M, N, K = map(int, sys.stdin.readline().split())

    matrix = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    stack = []
    cnt = 0

    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        matrix[Y][X] = 1

    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                dfs(i, j)

    print(cnt)
