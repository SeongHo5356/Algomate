import sys

input = sys.stdin.readline


def bfs(field: list[list[int]], m: int, n: int):
    M = len(field)
    N = len(field[0])
    stack = []
    stack.append((m, n))
    while stack:
        m, n = stack.pop()
        field[m][n] = 0
        for dm, dn in [(-1, 0), (0, -1), (+1, 0), (0, +1)]:
            nm, nn = m + dm, n + dn
            if nm < 0 or nm >= M:
                continue
            if nn < 0 or nn >= N:
                continue
            if field[nm][nn] == 0:
                continue
            stack.append((nm, nn))


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().rstrip().split(" "))
    field = [[0 for _ in range(N)] for _ in range(M)]
    for _ in range(K):
        m, n = map(int, input().rstrip().split(" "))
        field[m][n] = 1
    result = 0
    for m in range(M):
        for n in range(N):
            if field[m][n] == 0:
                continue
            bfs(field, m, n)
            result += 1
    print(result)
