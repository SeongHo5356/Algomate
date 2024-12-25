import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    M,N,K = map(int, input().split()) # 가로 M, 세로 N, 배추개수 K
    graph = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    for _ in range(K):
        x,y = map(int, input().split())
        graph[y][x] = 1

    dy=[0,1,0,-1]
    dx=[1,0,-1,0]

    def bfs(y,x):
        q=[]
        q.append((y,j))
        visited[y][j] = 1
        while q:
            cy,cx = q.pop(0)
            for k in range(4):
                ny=cy+dy[k]
                nx=cx+dx[k]
                if 0<=ny<N and 0<=nx<M and graph[ny][nx] == 1 and visited[ny][nx] ==0:
                    visited[ny][nx] = 1
                    q.append((ny,nx))
    ans=0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j] == 0:
                visited[i][j] = 1
                ans+=1
                bfs(i,j)
    print(ans)