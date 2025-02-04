import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def dfs(x,y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<=nx<M) and (0<=ny<N):
            if graph[ny][nx] == 1:
                graph[ny][nx] = 0
                dfs(nx,ny) 
    

T = int(input())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(T):
    count = 0
    M,N,K = map(int,input().split())
    graph = list([0]*M for _ in range(N))
    for i in range(K):
        s,f = map(int,input().split())
        graph[f][s] = 1
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                dfs(j,i)
                count+=1
    print(count)