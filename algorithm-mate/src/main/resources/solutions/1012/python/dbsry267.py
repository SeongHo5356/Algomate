import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    m, n, k = list(map(int, sys.stdin.readline().split()))
    cabbages = []
    visited = set()
    queue = []
    cnt = 0
    for _ in range(k):
        cabbages.append(tuple(map(int, sys.stdin.readline().split())))
    cabbageSet = set(cabbages)
    for i in cabbages:
        if i in visited:
            continue
        queue.append(i)
        visited.add(i)
        while len(queue) > 0:
            x, y = queue[0]
            if x + 1 < m:
                t = (x + 1, y)
                if t not in visited and t in cabbageSet:
                    queue.append(t)
                    visited.add(t)
            if x > 0:
                t = (x - 1, y)
                if t not in visited and t in cabbageSet:
                    queue.append(t)
                    visited.add(t)
            if y + 1 < n:
                t = (x, y + 1)
                if t not in visited and t in cabbageSet:
                    queue.append(t)
                    visited.add(t)
            if y > 0:
                t = (x, y - 1)
                if t not in visited and t in cabbageSet:
                    queue.append(t)
                    visited.add(t)
            del queue[0]
        cnt += 1
    print(cnt)