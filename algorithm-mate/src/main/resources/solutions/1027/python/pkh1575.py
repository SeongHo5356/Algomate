import sys

ssr = sys.stdin.readline
N = int(ssr())
l = list(map(int, ssr().split(' ')))


def solution(buildings):
    ret = 0
    if N == 1:
        return ret

    for i1, y1 in enumerate(buildings):
        temp = 0
        x1 = i1 + 1
        inc = None
        for i2 in range(i1 + 1, N):
            x2 = i2 + 1
            y2 = buildings[i2]
            a = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else 0
            if inc is None or inc < a:
                inc = a
                temp += 1

        inc = None
        for i2 in range(i1 - 1, -1, -1):
            x2 = i2 + 1
            y2 = buildings[i2]
            a = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else 0
            if inc is None or inc > a:
                inc = a
                temp += 1

        ret = max(temp, ret)

    return ret


print(solution(l))