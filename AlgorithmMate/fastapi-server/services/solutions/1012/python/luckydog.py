from sys import stdin
def input(): return stdin.readline().strip()
T = int(input())
def bfs(x,y):
    global M,N,matrix
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    l = [(x,y)]
    matrix[x][y] = 0
    while l:
        x,y = l.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if matrix[nx][ny]:
                l.append((nx,ny))
                matrix[nx][ny] = 0


for _ in range(T):
    M,N,K = map(int,input().split())
    matrix = [[0]*N for _ in range(M)]
    cnt = 0
    for _ in range(K):
        x,y = map(int,input().split())
        matrix[x][y] = 1

    for a in range(M):
        for b in range(N):
            if matrix[a][b]:
                bfs(a,b)
                cnt += 1
    print(cnt)
