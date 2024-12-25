from sys import stdin
T = int(stdin.readline().rstrip())

for i in range(T):
    M, N, K = map(int, stdin.readline().rstrip().split())
    cab = [[False for _ in range(N)] for __ in range(M)]
    for j in range(K):
        X, Y = map(int, stdin.readline().rstrip().split())
        cab[X][Y] = True
    bfs = []
    count = 0
    for x in range(M):
        for y in range(N):
            if cab[x][y]:
                bfs.append((x, y))
                while len(bfs) > 0:
                    p, q = bfs.pop(0)
                    cab[p][q] = False
                    if (p - 1) >= 0:
                        if cab[p - 1][q]:
                            cab[p - 1][q] = False
                            bfs.append((p - 1, q))
                    if (p + 1) < M:
                        if cab[p + 1][q]:
                            cab[p + 1][q] = False
                            bfs.append((p + 1, q))
                    if (q - 1) >= 0:
                        if cab[p][q - 1]:
                            cab[p][q - 1] = False
                            bfs.append((p, q - 1))
                    if (q + 1) < N:
                        if cab[p][q + 1]:
                            cab[p][q + 1] = False
                            bfs.append((p, q + 1))
                count += 1
    print(count)