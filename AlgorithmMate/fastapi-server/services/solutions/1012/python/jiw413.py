import sys
input = sys.stdin.readline


def DFS():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    visited = [[False]*M for _ in range(N)]
    count = 0
    for x, y in start:
        if not visited[y][x]:
            stack = [(x, y)]
            visited[y][x] = True
            while stack:
                now_x, now_y = stack.pop()
                for go in range(4):
                    next_x = now_x + dx[go]
                    next_y = now_y + dy[go]
                    if 0 <= next_x < M and 0 <= next_y < N and not visited[next_y][next_x] and all[next_y][next_x] != 0:
                        stack.append((next_x, next_y))
                        visited[next_y][next_x] = True
            count += 1
    return count



T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    all = [[0]*M for _ in range(N)]
    start = []
    for i in range(K):
        x, y = map(int, input().split())
        start.append((x, y))
        all[y][x] = 1
    print(DFS())