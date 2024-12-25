import sys

def find_worm(x, y, m, n, farm):
    # 스택을 사용한 DFS 구현
    stack = [(x, y)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상, 하, 좌, 우 방향

    while stack:
        cx, cy = stack.pop()
        
        if cx < 0 or cx >= m or cy < 0 or cy >= n:
            continue
        if farm[cy][cx] == 0:
            continue
        
        farm[cy][cx] = 0  # 현재 위치를 방문했음을 표시

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            stack.append((nx, ny))  # 다음 좌표를 스택에 추가


t = int(sys.stdin.readline().strip())

for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().strip().split())
    farm = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        farm[y][x] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if farm[i][j] == 1:
                result += 1
                find_worm(j, i, m, n, farm)

    print(result)