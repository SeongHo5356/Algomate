import sys
input = sys.stdin.readline

def check(i, j, cabbage, visit, n, m):
    if (0 <= i < n) and (0 <= j < m) and (visit[i][j] == 0) and (cabbage[i][j] != 0):
        return True
    else:
        return False

def DFS(i,j, cabbage, visit, n, m):

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    stack = []
    stack.append([i,j])

    while stack:
        x, y = stack.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if check(nx, ny, cabbage, visit, n, m):
                visit[nx][ny] = 1
                stack.append([nx, ny])

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    cabbage = [[0] * m for _ in range(n)]
    visit = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        cabbage[b][a] = 1

    answer = 0
    for i in range(n):
        for j in range(m):
            if check(i, j, cabbage, visit, n, m):
                answer += 1
                # print(f"{i} {j}")
                DFS(i, j, cabbage, visit, n, m)
    print(answer)
