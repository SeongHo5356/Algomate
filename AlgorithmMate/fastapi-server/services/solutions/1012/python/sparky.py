import sys

input = sys.stdin.readline

T = int(input())
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for _ in range(T):
    M, N, K = map(int, input().split())
    cabbages = set()
    for _ in range(K):
        x, y = map(int, input().split())
        cabbages.add((x, y))

    count = 0

    while cabbages:
        bugs = [cabbages.pop()]

        while bugs:
            x, y = bugs.pop()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if (nx, ny) in cabbages:
                    cabbages.discard((nx, ny))
                    bugs.append((nx, ny))

        count += 1

    print(count)

        