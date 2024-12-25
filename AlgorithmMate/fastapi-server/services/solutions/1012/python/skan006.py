import sys

def solution():
    t = int(sys.stdin.readline().rstrip())
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for _ in range(t):
        m, n, k = map(int, sys.stdin.readline().split())
        cabbages = set()
        for _ in range(k):
            x, y = map(int, sys.stdin.readline().split())
            cabbages.add((x, y))

        count = 0
        while cabbages:
            bug_Stomach = [cabbages.pop()]

            while bug_Stomach:
                x, y = bug_Stomach.pop()
                for dx, dy in directions:
                    nx, ny = x+dx, y+dy
                    if (nx, ny) in cabbages:
                        cabbages.discard((nx, ny))
                        bug_Stomach.append((nx, ny))
            count += 1
        sys.stdout.write(str(count)+'\n')

solution()