import sys
sys.setrecursionlimit(10000)  # 재귀 한도를 필요에 따라 증가시킵니다.
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
input = sys.stdin.readline

def dfs(x, y, chk, adj):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 경계 체크를 먼저 수행한 후에 인덱스에 접근합니다.
        if 0 <= nx < len(adj[0]) and 0 <= ny < len(adj) and adj[ny][nx] and not chk[ny][nx]:
            chk[ny][nx] = True
            dfs(nx, ny, chk, adj)

T = int(input())
for _ in range(T):
    M, N, cnt = map(int, input().split())
    adj = [[False] * M for _ in range(N)]
    for _ in range(cnt):
        a, b = map(int, input().split())
        adj[b][a] = True
    chk = [[False] * M for _ in range(N)]
    ans = 0

    for i in range(M):
        for j in range(N):
            if adj[j][i] and not chk[j][i]:
                ans += 1
                chk[j][i] = True
                dfs(i, j, chk, adj)

    print(ans)
