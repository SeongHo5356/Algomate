import sys

input = sys.stdin.readline

t = int(input().strip())

def bfs(matrix, x, y):
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    stack = [(x, y)]
    matrix[x][y] = 0

    while stack:
        a, b = stack.pop()
        for dx, dy in move:
            nx, ny = a + dx, b + dy

            if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] == 1:
                stack.append((nx, ny))
                matrix[nx][ny] = 0

for _ in range(t):
    m, n, k = map(int, input().strip().split())

    field = [[0] * n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().strip().split())
        field[x][y] = 1

    cnt = 0
    for i in range(m):
        for j in range(n):
            if field[i][j] == 1:
                cnt += 1
                bfs(field, i, j)

    print(cnt)
