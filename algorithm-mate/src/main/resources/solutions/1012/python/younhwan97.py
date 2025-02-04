import sys
input = sys.stdin.readline

sys.setrecursionlimit(10000)

# 이동방향(상, 하, 좌, 우)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def search(graph, visited, xx, yy, M, N):
    # 방문처리
    visited[yy][xx] = 0
    
    for i in range(4):
        nx = xx + dx[i]
        ny = yy + dy[i]

        if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] != 0 and graph[ny][nx] == 1:
            search(graph, visited, nx, ny, M, N)

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1
        visited[y][x] = 1

    # 필요한 갯수
    cnt = 0

    # 탐색
    for xx in range(M):
        for yy in range(N):
            # 아직 방문하지 않았을 때 
            if visited[yy][xx] != 0:
                cnt += 1
                search(graph, visited, xx, yy, M, N)
        
    print(cnt)