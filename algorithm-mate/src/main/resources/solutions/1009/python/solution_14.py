from sys import stdin

iter_count = {0: 1, 1: 1, 2: 4, 3: 4, 4: 2, 5: 1, 6: 1, 7: 4, 8: 4, 9: 2}
answer = {
    0: {0 :10},
    1: {0 :1},
    2: {1: 2, 2: 4, 3: 8, 0: 6},
    3: {1: 3, 2: 9, 3: 7, 0: 1},
    4: {1: 4, 0: 6},
    5: {0 :5},
    6: {0 :6},
    7: {1: 7, 2: 9, 3: 3, 0: 1},
    8: {1: 8, 2: 4, 3: 2, 0: 6},
    9: {1: 9, 0: 1},
}

t = int(stdin.readline())
for _ in range(t):
    a, b = map(int, stdin.readline().split())
    n = a % 10
    m = b % iter_count[n]
    print(answer[n][m])
