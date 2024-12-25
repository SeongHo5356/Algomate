import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dirY = [-1,1,0,0]
dirX = [0,0,-1,1]

def dfs(y,x):
    global visited, graph
    visited[y][x] = True

    for i in range(4):
        newY = y + dirY[i]
        newX = x + dirX[i]
        if graph[newY][newX] and not visited[newY][newX]:
            dfs(newY, newX)

T = int(input())
MAX = 50+10

while T>0:
    T-=1
    M,N,K = map(int,input().split())
    graph = [[False]*(M+2) for _ in range(N+2)]
    visited = [[False]*(M+2) for _ in range(N+2)]


    for _ in range(K):
        x, y = map(int, input().split())
        graph[y+1][x+1] = True

    answer = 0
    for i in range(1,N+1):
        for j in range(1,M+1):
            if graph[i][j]==True and not visited[i][j]:
                dfs(i,j)
                answer+=1
    print(answer)