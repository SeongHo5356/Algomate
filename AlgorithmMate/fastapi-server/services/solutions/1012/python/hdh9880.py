import sys
input = sys.stdin.readline

mod_x = [-1, 1, 0, 0]
mod_y = [0, 0, -1, 1]
t = int(input())


def BFS(y, x):
    queue = [(y, x)]
    cabbages[y][x] = 2
    while queue:
        y, x = queue.pop(0)
        for i in range(4):
            new_x = x + mod_x[i]
            new_y = y + mod_y[i]
            if 0 <= new_x < m and 0 <= new_y < n and cabbages[new_y][new_x] == 1:
                queue.append((new_y, new_x))
                cabbages[new_y][new_x] = 2


for _ in range(t):
    cnt = 0
    m, n, k = map(int, input().split())
    cabbages = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        cabbages[y][x] = 1
    for i in range(n):
        for j in range(m):
            if cabbages[i][j] == 1:
                BFS(i, j)
                cnt += 1
    print(cnt)



