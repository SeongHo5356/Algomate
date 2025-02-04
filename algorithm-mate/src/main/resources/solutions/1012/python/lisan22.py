import sys

input = sys.stdin.readline
T = int(input())
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
answer = []


def bfs(j, i):
    queue = [(j, i)]
    # cnt = 1
    while queue:
        y, x = queue.pop()
        # cnt += 1
        visited[y][x] = True
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < M:

                if not visited[ny][nx] and board[ny][nx]:
                    queue.append((ny, nx))
    # return cnt


for t in range(T):
    N, M, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    visited = [[False] * M for _ in range(N)]
    for i in range(K):
        y, x = map(int, input().split())
        board[y][x] = 1
    worm = 0
    for j in range(N):
        for i in range(M):
            if board[j][i] and not visited[j][i]:
                bfs(j, i)
                worm += 1
    answer.append(worm)
for a in answer:
    print(a)