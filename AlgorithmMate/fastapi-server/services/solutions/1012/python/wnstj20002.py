import sys
sys.setrecursionlimit(10**6) 
input=sys.stdin.readline

def dfs(y1,x1):
    global visited
    global graph
    visited[y1][x1]=1
    if visited[y1+1][x1]==0 and graph[y1+1][x1]==1:
        dfs(y1+1,x1)
    if visited[y1-1][x1]==0 and graph[y1-1][x1]==1:
        dfs(y1-1,x1)
    if visited[y1][x1+1]==0 and graph[y1][x1+1]==1:
        dfs(y1,x1+1)
    if visited[y1][x1-1]==0 and graph[y1][x1-1]==1:
        dfs(y1,x1-1)
    

    



t=int(input())
for _ in range(t):
    count=0
    m,n,k=map(int,input().split()) # m=x n=y    
    graph=[[0]*(m+2) for _ in range(n+3)]
    visited=[[0]*(m+2) for _ in range(n+3)]

    for _ in range(k):
        x,y=map(int,input().split())
        graph[y+1][x+1]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if graph[i][j]==1 and visited[i][j]==0:
                dfs(i,j)
                count+=1
    print(count)
