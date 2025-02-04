import sys

# 테스트 케이스
t = int(sys.stdin.readline())

def dfs_stack(row, col):
    stack = [(row, col)]
    visited[row][col] = True

    while stack:
        row, col = stack.pop()

        # 상, 하, 좌, 우
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            # 바운더리 체크
            # 1인지 체크
            # 방문 안했는지 체크
            if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] == 1 and not visited[nr][nc]:
                stack.append((nr, nc))
                visited[nr][nc] = True


# 주어진 테스트 케이스만큼 반복
for _ in range(t):
    # 가로 길이(열) m, 세로 길이(행) n, 배추가 심어져 있는 위치의 개수 k 입력
    m, n, k = map(int, sys.stdin.readline().split())

    # 2중 배열에서 겉의 리스트는 행, 안의 리스트는 열이 된다.
    graph = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(k):
        col, row = map(int, sys.stdin.readline().split())
        graph[row][col] = 1

    visited = [[False for _ in range(m)] for _ in range(n)]

    count = 0

    for row in range(n):
        for col in range(m):
            if graph[row][col] == 1 and not visited[row][col]:
                dfs_stack(row, col)
                count += 1

    print(count)


