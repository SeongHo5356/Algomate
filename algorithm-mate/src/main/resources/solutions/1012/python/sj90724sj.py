import sys

T = int(sys.stdin.readline())

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    array = [[0] * (M + 2) for i in range(N + 2)]

    for j in range(K):
        x, y = map(int, sys.stdin.readline().split())

        array[y + 1][x + 1] = 1

    num = 0
    for n in range(1, N + 2):
        for m in range(1, M + 2):
            if array[n][m] == 1:
                y = n
                x = m
                array[y][x] = 2
                path = [(x, y)]

                while True:
                    # 북 확인
                    if array[y - 1][x] == 1:
                        path.append((x, y - 1))
                        array[y - 1][x] = 2
                        y = y - 1
                    # 동 확인
                    elif array[y][x + 1] == 1:
                        path.append((x + 1, y))
                        array[y][x + 1] = 2
                        x = x + 1
                    # 남 확인
                    elif array[y + 1][x] == 1:
                        path.append((x, y + 1))
                        array[y + 1][x] = 2
                        y = y + 1
                    # 서 확인
                    elif array[y][x - 1] == 1:
                        path.append((x - 1, y))
                        array[y][x - 1] = 2
                        x = x - 1
                    # 다 없음
                    else:
                        if len(path) == 0:
                            num += 1
                            break
                        else:
                            path.pop()
                            if len(path) != 0:
                                x, y = path[len(path) - 1]


    print(num)
