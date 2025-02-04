import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if(0 <= nx < m) and (0 <= ny < n):
            if a[nx][ny] == 1:
                a[nx][ny] = 0
                dfs(nx, ny)

t = int(input())

for i in range(t):
    m, n, k = map(int, input().split())
    a = [[0]*n for i in range(m)]
    count = 0
    for j in range(k):
        b, c = map(int, input().split())
        a[b][c] = 1
    for x in range(m):
        for y in range(n):
            if a[x][y] == 1:
                dfs(x, y)
                count += 1
    print(count)