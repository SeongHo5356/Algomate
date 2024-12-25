import sys
sys.setrecursionlimit(10**9) #1
t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [ [0]*m for _ in range(n) ] #2
    visit = [ [False]*m for _ in range(n) ] #2
    cnt = 0
    dx = [ 0, 0, -1, 1 ] #3
    dy = [ -1, 1, 0, 0 ]
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().split())
        graph[b][a] = 1 #4
    def dfs(x, y):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and visit[nx][ny] == False:
                    visit[nx][ny] = True
                    dfs(nx, ny)

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visit[i][j] == False:
                visit[i][j] = True #5
                dfs(i, j)
                cnt += 1 #6
    print(cnt)