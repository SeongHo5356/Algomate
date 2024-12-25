import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

T = int(input())
mv = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def dfs(start, visit):
    sc, sr = start[0], start[1]
    visit[sr][sc] = True

    for m in mv:
        nc, nr = sc + m[0], sr + m[1]
        if 0 <= nc < M and 0 <= nr < N:
            if farm[nr][nc] and not visit[nr][nc]:
                dfs((nc, nr), visit)


for _ in range(T):
    M, N, K = map(int, input().split())
    farm = list([0] * M for _ in range(N))
    visited = list([False] * M for _ in range(N))

    cnt = 0
    for _ in range(K):
        c, r = map(int, input().split())
        farm[r][c] = 1

    for i in range(N):
        for j in range(M):
            if farm[i][j] and not visited[i][j]:
                dfs((j, i), visited)
                cnt += 1
    
    print(cnt)