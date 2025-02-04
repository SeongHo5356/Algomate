import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m,n,k = map(int,input().split()) # m = 10 , n = 8
    graph = [[0]*m for _ in range(n)]

    # 그래프 초기화
    for _ in range(k):
        a,b = map(int,input().split())
        graph[b][a] = 1
        
    # visited 초기화
    visited = [[False]*m for _ in range(n)]
        
    da = [-1,1,0,0] 
    db = [0,0,-1,1]
    def bfs(a,b):
        que = [(a,b)]
        while que:
            ea, eb = que.pop(0)
            for k in range(4):
                na = ea + da[k]
                nb = eb + db[k]
                if 0<=na<n and 0<=nb <m:
                    if not visited[na][nb] and graph[na][nb]:
                        visited[na][nb]=True
                        que.append((na,nb))
            
        
    warm = 0
    for j in range(n):
        for i in range(m):
            if graph[j][i] ==1 and not visited[j][i]:
                visited[j][i]= True
                warm +=1
                bfs(j,i)
    print(warm)
    

        
    
    