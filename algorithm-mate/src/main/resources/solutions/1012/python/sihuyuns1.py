import sys

T = int(sys.stdin.readline().strip())  

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(T):
    M, N, K = map(int,sys.stdin.readline().split())
    graph = [[0] * N for _ in range(M)]
    que = []
    res = 0
    
    for i in range(K):
        X, Y = map(int,sys.stdin.readline().split())
        # print("(X, Y)", X, Y)
        graph[X][Y] = 1

    def bfs():
        while len(que):
            x, y = que.pop(0)
            for k in range(4):
                X = x + dx[k]
                Y = y + dy[k]
                if X < 0 or Y < 0 or X >= M or Y >= N:
                    continue
                if graph[X][Y] == 1:
                    que.append((X, Y))
                    graph[X][Y] = 0
                    # print(graph[X][Y])
                    
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                res += 1
                que.append((i, j))
                graph[i][j] = 0
                bfs()
                
    print(res)