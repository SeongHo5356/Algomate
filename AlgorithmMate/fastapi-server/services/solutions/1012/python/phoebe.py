import sys

sys.setrecursionlimit(10000)

def dfs(i, j): 
    visited[i][j] = True
    # 아래쪽 탐색
    if i + 1 < N and not visited[i + 1][j] and arr[i + 1][j] == 1:
        dfs(i + 1, j)
    # 위쪽 탐색
    if i - 1 >= 0 and not visited[i - 1][j] and arr[i - 1][j] == 1:
        dfs(i - 1, j)
    # 오른쪽 탐색
    if j + 1 < M and not visited[i][j + 1] and arr[i][j + 1] == 1:
        dfs(i, j + 1)
    # 왼쪽 탐색
    if j - 1 >= 0 and not visited[i][j - 1] and arr[i][j - 1] == 1:
        dfs(i, j - 1)
    else:
        return    

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    arr = [[0] * M for _ in range(N)]  # 배추의 위치
    visited = [[False] * M for _ in range(N)]
    count = 0  # 컴포넌트(군집)의 수

    # 배추의 위치 입력
    for _ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        arr[Y][X] = 1

    # 모든 위치를 탐색하며 DFS 호출
    for i in range(N):
        for j in range(M):
            if not visited[i][j] and arr[i][j] == 1:
                count += 1
                dfs(i, j)     
    print(count)