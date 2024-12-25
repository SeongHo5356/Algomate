import sys

def find_baechu(N, M):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if field[i][j] == 1:
                # 배추 발견하면 DFS로 연결된 배추를 확인
                # DFS로 연결된 배추들을 확인하고 확인표시를 해서, 이후에 다시 탐색할 일 없도록 했음
                # DFS로 탐색하는 횟수가 결국 벌레의 수
                DFS(i, j, N, M)
                cnt += 1
    return cnt

def DFS(si, sj, N, M):
    global visited
    global field
    stack = []

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    visited[si][sj] = 1
    i, j = si, sj
    while 1:
        field[i][j] = 2
        # 혼선 방지를 위해서 지나온 배추는 2으로 변경
        for k in range(4):
            mi, mj = i + di[k],j  + dj[k]
            if 0 <= mi < N and 0 <= mj < M and visited[mi][mj] == 0 and field[mi][mj] == 1:
                stack.append((i, j))
                i, j = mi, mj
                visited[i][j] = 1
                break
        else:
            if stack:
                i, j = stack.pop()
            else:
                return
    return

############################################################

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    # M 가로 / N 세로 / K 배추 심겨진 개수
    field = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for __ in range(K):
        j, i = map(int, sys.stdin.readline().split())
        field[i][j] += 1

    print(find_baechu(N, M))