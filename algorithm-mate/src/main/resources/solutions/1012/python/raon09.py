import sys
sys.setrecursionlimit(10000)
def dfs(i, j):
    farm[i][j] = 0
    if i > 0 and farm[i-1][j] == 1:
        dfs(i-1, j)
    if i < n-1 and farm[i+1][j] == 1:
        dfs(i+1, j)
    if j > 0 and farm[i][j-1] == 1:
        dfs(i, j-1)
    if j < m-1 and farm[i][j+1] == 1:
        dfs(i, j+1)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    farm = [[0 for i in range(m)] for j in range(n)]
    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        farm[y][x] = 1
    sum = 0
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                sum += 1
                dfs(i, j)
    print(sum)