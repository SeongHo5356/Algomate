import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    m, n, k = list(map(int,input().split()))

    farm = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = list(map(int,input().split()))
        farm[y][x] = 1
    
    visited = [[False for _ in range(m)] for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 0 or visited[i][j]:
                continue
            
            stack = [(i,j)]
            visited[i][j] = True
            while stack:
                cx, cy = stack.pop()
                for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                    nx = cx+dx
                    ny = cy+dy

                    if 0 <= nx < n and 0 <= ny < m and farm[nx][ny] == 1 and not visited[nx][ny]:
                        stack.append((nx,ny))
                        visited[nx][ny] = True

            answer += 1
            # print(visited)
    
    print(answer)
