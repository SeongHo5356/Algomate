import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

t = int(input())
MAX = 60

dirR = [1,-1,0,0]
dirC = [0,0,1,-1]

def dfs(y,x):
    global visited
    visited[y][x] = 1
    for i in range(4):
        new_x = x + dirR[i]
        new_y = y + dirC[i]
        if graph[new_y][new_x] and not visited[new_y][new_x]:
            dfs(new_y,new_x)

for _ in range(t):
    m,n,k = map(int, input().split())
    graph = [[0]*MAX for _ in range(MAX)]
    visited = [[0]*MAX for _ in range(MAX)]
    
    for _ in range(k):
        x,y = map(int, input().split())
        graph[y+1][x+1] = 1
    
    ans = 0
    
    for y in range(n+1):
        for x in range(m+1):
            if graph[y][x] and not visited[y][x]:
                ans += 1
                dfs(y,x)
    print(ans)
    

        
        