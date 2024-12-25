import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0] # 상하좌우 이동하여 계산하기 위한 list
dy = [0, 0, -1, 1]

def dfs(y, x):
  for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if (0 <= nx < m) and (0 <= ny <n):
          if graph[ny][nx] == 1:
            graph[ny][nx] = 0
            dfs(ny, nx)


T = int(input())
for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    answer = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                dfs(i,j)
                answer += 1
    print(answer)