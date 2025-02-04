import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def DFS(y, x):
    visited[y][x] = True
    if x > 0 and farm[y][x-1] == True and visited[y][x-1] == False:
        DFS(y, x-1)
    if x < M-1 and farm[y][x+1] == True and visited[y][x+1] == False:
        DFS(y, x+1)
    if y > 0 and farm[y-1][x] == True and visited[y-1][x] == False:
        DFS(y-1, x)
    if y < N-1 and farm[y+1][x] == True and visited[y+1][x] == False:
        DFS(y+1, x)
    return

T = int(input())
for i in range(T):
    M, N, K = map(int, input().split())
    farm = [[False for a in range(M)] for b in range(N)]
    visited = [[False for a in range(M)] for b in range(N)]
    count = 0
    for j in range(K):
        X, Y = map(int, input().split())
        farm[Y][X] = True
    for k in range(N):
        for l in range(M):
            if farm[k][l] == True and visited[k][l] == False:
                DFS(k, l)
                count += 1
    print(count)