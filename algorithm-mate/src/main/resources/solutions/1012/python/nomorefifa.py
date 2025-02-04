import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

max = 50 + 2
diry = [-1, 1, 0, 0]
dirx = [0, 0, -1, 1]

def dfs(y, x):
    global visited
    visited[y][x] = True
    for i in range(4):
        newx = x + dirx[i]
        newy = y + diry[i]
        if arr[newy][newx] and not visited[newy][newx]:
            dfs(newy, newx)

t = int(input())

for a in range(t):
    m, n, k = map(int, input().split())
    arr = [[False] * (max) for _ in range(max)]
    visited = [[False] * (max) for _ in range(max)]
    for b in range(k):
        x, y = map(int, input().split())
        arr[y + 1][x + 1] = True
    ans = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if arr[i][j] and not visited[i][j]:
                dfs(i, j)
                ans += 1    
    print(ans)