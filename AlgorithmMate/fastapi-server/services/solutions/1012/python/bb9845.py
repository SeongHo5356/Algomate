#1012번
import sys

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS(x, y):
    queue = [[x,y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            q = a + dx[i]
            w = b + dy[i]
            if (0 <= q < N and 0 <= w < M and field[q][w] == 1):
                field[q][w] = 0
                queue.append([q,w])
        

T = int(input())

for i in range(T):
    cnt = 0
    #M:가로길이, N:세로길이, K:배추 개
    M, N, K = map(int,sys.stdin.readline().split())
    field = [[0]*M for _ in range(N)]
    for j in range(K):
        #X, Y:배추위치
        X, Y = map(int,sys.stdin.readline().split())
        field[Y][X] = 1
    for k in range(N):
        for n in range(M):
            if field[k][n] == 1:
                BFS(k,n)
                field[k][n] = 0
                cnt += 1
    print(cnt)