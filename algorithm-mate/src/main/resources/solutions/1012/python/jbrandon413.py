import sys

input = sys.stdin.readline


def bfs(x, y):
    q = [[y,x]]
    arr[y][x] = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        n = q.pop(0)
        cy = n[0]
        cx = n[1]
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < M and 0 <= ny < N and arr[ny][nx] == 1:
                q.append([ny, nx])
                arr[ny][nx] = 0


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for i in range(N)]
    cnt = 0
    for i in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1:
                bfs(x, y)
                cnt += 1
    print(cnt)