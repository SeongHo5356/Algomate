import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


t = int(input())

def dfs(x, y):

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):

        nx = dx[i] + x
        ny = dy[i] + y

        if nx < 0 or nx>=n or ny<0 or ny>=m:
            continue

        if graph[nx][ny] == 1:
            graph[nx][ny] = 0
            dfs(nx, ny)



for _ in range(t):

    m, n, k = map(int, input().split())

    graph = [[0]*m for _ in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1


    count = 0
    for a in range(n):
        for b in range(m):
            if graph[a][b] == 1:
                dfs(a, b)
                count +=1
    print(count)






    
