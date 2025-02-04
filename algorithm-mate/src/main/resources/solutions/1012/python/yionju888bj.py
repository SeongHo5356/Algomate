import sys

def solve():
    # readline으로 한 줄씩 입력 받기

    T = int(sys.stdin.readline().strip())  # 테스트 케이스의 개수 입력 받기
    results = []

    for _ in range(T):
        M, N, K = map(int, sys.stdin.readline().strip().split())  # M, N, K 값 입력 받기
        field = [[0] * M for _ in range(N)]  # 배추밭 초기화
        for _ in range(K):
            x, y = map(int, sys.stdin.readline().strip().split())  # 배추 위치 입력 받기
            field[y][x] = 1

        visited = [[False] * M for _ in range(N)]  # 방문 여부 초기화
        count = 0

        # DFS로 배추 뭉치 개수 세기
        def dfs(x, y):
            stack = [(x, y)]
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while stack:
                cx, cy = stack.pop()
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and field[nx][ny] == 1:
                        visited[nx][ny] = True
                        stack.append((nx, ny))

        for i in range(N):
            for j in range(M):
                if field[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    dfs(i, j)
                    count += 1

        results.append(count)

    for result in results:
        print(result)


solve()