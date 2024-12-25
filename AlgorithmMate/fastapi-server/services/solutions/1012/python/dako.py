import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def DFS(x,y):
    A[x][y] = 0
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if A[nx][ny] == 1:
                DFS(nx, ny)

for _ in range(T):
    M, N, K = map(int, input().split())
    A = [[0]*M for _ in range(N)]
    cnt = 0
    for _ in range(K):
        x, y = map(int, input().split())
        A[y][x] = 1
    for i in range(N):
        for j in range(M):
            if A[i][j] == 1:
                DFS(i,j)
                cnt += 1
    print(cnt)