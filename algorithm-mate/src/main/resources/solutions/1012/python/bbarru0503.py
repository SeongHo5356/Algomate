import sys
input = sys.stdin.readline

def bfs():
    ans = 0
    queue = []

    for i in range(n):
        for j in range(m):
            if map_[i][j] and not visited[i][j]:
                queue.append((i, j))
                visited[i][j] = True

                while queue:
                    ci, cj = queue.pop(0)

                    for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        ni, nj = ci + di, cj + dj
                        if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and map_[ni][nj]:
                            visited[ni][nj] = True
                            queue.append((ni, nj))

                    if not queue:
                        ans += 1

    return ans

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        m, n, k = map(int, input().split())
        map_ = [[False]*m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]
        for _ in range(k):
            y, x = map(int, input().split())
            map_[x][y] = True
        print(bfs())