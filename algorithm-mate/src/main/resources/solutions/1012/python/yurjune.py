import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(sx, sy):
    for i in range(4):
        nx = sx + dx[i]
        ny = sy + dy[i]
        if nx<0 or ny<0 or nx>=m or ny>=n: continue
        if graph[ny][nx] == 0: continue

        graph[ny][nx] = 0
        dfs(nx, ny)

t = int(input())
for _ in range(t):
    m,n,k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for y in range(n):
        for x in range(m):
            if graph[y][x] != 0:
                dfs(x, y)
                count += 1

    print(count)