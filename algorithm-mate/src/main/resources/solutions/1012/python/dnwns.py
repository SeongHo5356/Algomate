import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i, j):
    if 0 <= i < n and 0 <= j < m and field[i][j] == 1:
        field[i][j] = 0
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
    return

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    field = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1

    bugs = 0
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                dfs(i, j)
                bugs += 1
    
    print(bugs)