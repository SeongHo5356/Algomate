import sys
input = sys.stdin.read
sys.setrecursionlimit(10000)


data = input().strip().splitlines()
T = int(data[0])
index = 1

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, field, visited, N, M):
    stack = [(x,y)]
    visited[x][y] = True
    
    while stack:
        cx, cy = stack.pop()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0<=nx<N and 0<=ny<M and not visited[nx][ny] and field[nx][ny] == 1:
                visited[nx][ny] = True
                stack.append((nx, ny))
results = []                
for _ in range(T):
    M, N, K = map(int, data[index].split())
    index += 1
    
    field = [[0]*M for i in range(N)]
    visited = [[False]*M for i in range(N)]
    
    for i in range(K):
        x, y = map(int, data[index].split())
        field[y][x] = 1
        index += 1
        
    worm_count = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]:
                dfs(i, j, field, visited, N, M)
                worm_count += 1
    
    
    results.append(worm_count)            
    
for i in results:
    print(i)
            