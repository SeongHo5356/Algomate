import sys
dydx = [(0, 1), (0, -1), (1, 0), (-1, 0)]
def dfs(field, y, x):
    stack = [(y, x)]
    while stack:
        nowy, nowx = stack.pop()
        if field[nowy][nowx]==1:
            field[nowy][nowx] = 0
        for dy, dx in dydx:
            nexty, nextx = nowy + dy, nowx + dx
            if 0<= nexty< n and 0<=nextx<m and field[nexty][nextx]==1:
                stack.append((nexty, nextx))

t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    field = [[0]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        field[y][x] = 1
    answer = 0
    for i in range(n):
        for j in range(m):
            if field[i][j]==1:
                dfs(field, i, j)
                answer+=1
    print(answer)