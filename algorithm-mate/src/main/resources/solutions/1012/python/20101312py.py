import sys
t = int(sys.stdin.readline().strip())

for i in range(t):
    ans = 0
    m, n, k = map(int, sys.stdin.readline().strip().split())
    visited = [[True for _ in range(n + 2)] for _ in range(m + 2)]
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().strip().split())
        visited[a + 1][b + 1] = False
    for x in range(m + 1):
        for y in range(n + 1):
            if not visited[x][y]:
                visited[x][y] = True
                ans += 1
                q = [[x, y]]
                while q:
                    curr_x, curr_y = q.pop(0)
                    move_to = [[curr_x - 1, curr_y], [curr_x + 1, curr_y], [curr_x, curr_y - 1], [curr_x, curr_y + 1]]
                    for to_x, to_y in move_to:
                        if not visited[to_x][to_y]:
                            q.append([to_x, to_y])
                            visited[to_x][to_y] = True

    print(ans)