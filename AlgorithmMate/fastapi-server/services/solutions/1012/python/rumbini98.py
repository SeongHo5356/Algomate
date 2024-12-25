import sys 

input = sys.stdin.readline


T = int(input())

for _ in range(T):

    M, N, K = map(int,input().split())


    field = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int,input().split())
        field[y][x] = 1

    def dfs(field, visited, x, y):
        stack = [(x, y)]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while stack:
            cx, cy = stack.pop()
            for dx, dy in directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < len(field) and 0 <= ny < len(field[0]) and not visited[nx][ny] and field[nx][ny] == 1:
                    visited[nx][ny] = True
                    stack.append((nx, ny))


    count = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                dfs(field, visited, i, j)
                count += 1

    print(count)


