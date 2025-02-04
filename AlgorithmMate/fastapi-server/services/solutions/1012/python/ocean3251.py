import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
MAX = 60  # 50 + 여유 공간

dirR = [1, -1, 0, 0]
dirC = [0, 0, 1, -1]  # 상하우좌 체크

def dfs_iterative(x, y):
    global visited
    stack = [(x, y)]
    visited[y][x] = True
    while stack:
        curr_x, curr_y = stack.pop()
        for dirIdx in range(4):
            newY = curr_y + dirR[dirIdx]
            newX = curr_x + dirC[dirIdx]
            if 0 <= newY < MAX and 0 <= newX < MAX and graph[newY][newX] and not visited[newY][newX]:
                visited[newY][newX] = True
                stack.append((newX, newY))

# 0. 입력 및 초기화
T = int(input().strip())
for _ in range(T):
    M, N, K = map(int, input().strip().split())
    graph = [[False] * MAX for _ in range(MAX)]
    visited = [[False] * MAX for _ in range(MAX)]

    # 1. 그래프 정보 입력
    for _ in range(K):
        x, y = map(int, input().strip().split())
        graph[y + 1][x + 1] = True

    # 2. 방문하지 않은 지점부터 dfs 돌기
    answer = 0
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if graph[i][j] and not visited[i][j]:
                dfs_iterative(j, i)  # x, y 순서로 호출
                answer += 1
    print(answer)
