import sys
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x,y):
    queue = [(x,y)]
    matrix[x][y] = 0
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if matrix[nx][ny] == 1:
                queue.append((nx,ny))
                matrix[nx][ny] = 0
TC = int(sys.stdin.readline().strip())
for i in range(TC):
    m,n,k = map(int, sys.stdin.readline().split())
    matrix = [[0]*n for _ in range(m)]
    count = 0
    for j in range(k):
        x,y = map(int, sys.stdin.readline().split())
        matrix[x][y] = 1
    for l in range(m):
        for p in range(n):
            if matrix[l][p] == 1:
                bfs(l,p)
                count += 1
    print(count)