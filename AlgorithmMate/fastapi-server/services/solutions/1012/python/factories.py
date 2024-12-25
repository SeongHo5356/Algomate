import sys

sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(x,y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False
    if farm[x][y] == 1:
        farm[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y -1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

    return False
t = int(input())
re = 0
for _ in range(t):
    M,N,k = map(int, input().split())
    farm = [[0] * M for i in range(N)]
    for s in range(k):
        x,y = map(int, input().split())
        farm[y][x] = 1
    for i in range(N):
        for j in range(M):
            if dfs(i,j) == True:
                re += 1
    print(re)
    re = 0