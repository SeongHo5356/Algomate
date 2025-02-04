import sys
input = sys.stdin.readline  # 빠른 입력을 위해 sys.stdin.readline 사용

row = [-1, 1, 0, 0]
col = [0, 0, 1, -1]

def bfs(i, j, n, m):
    queue = []
    queue.append((i, j))
    bechu[i][j] = 0
    while queue:
        cur = queue.pop(0)
        # 상하좌우 탐색
        for k in range(4):
            r = cur[0] + row[k]
            c = cur[1] + col[k]
            if r < 0 or c < 0 or r >= m or c >= n:
                continue
            # 배추면 연결해서 가야하므로 큐에 넣기!
            if bechu[r][c] == 1:
                queue.append((r, c))
                # 이 배추는 방문처리
                bechu[r][c] = 0

if __name__ == '__main__':
    TC = int(input())
    for _ in range(TC):
        answer = 0
        # 가로, 세로, 배추개수
        m, n, k = map(int, input().split())
        bechu = [[0] * n for _ in range(m)]
        for _ in range(k):
            x, y = map(int, input().split())
            bechu[x][y] = 1

        for i in range(m):
            for j in range(n):
                if bechu[i][j] == 1:
                    answer += 1
                    bfs(i, j, n, m)
        print(answer)
