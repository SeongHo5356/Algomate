# Question URL: https://www.acmicpc.net/problem/1012

def check_neighbor(x, y, x_limit, y_limit):
## x, y: 확인을 시작하는 좌표
## x_limit, y_limit: 배열의 크

##    좌측 체크
    if x - 1 >= 0:
        if ar[x - 1][y] == 1:

            ar[x - 1][y] = 0
            check_neighbor(x - 1, y, x_limit, y_limit)
##    우측 체크
    if x + 1 < x_limit:
        if ar[x + 1][y] == 1:
            
            ar[x + 1][y] = 0
            check_neighbor(x + 1, y, x_limit, y_limit)
##    상단 체크
    if y + 1 < y_limit:
        if ar[x][y + 1] == 1:
            
            ar[x][y + 1] = 0
            check_neighbor(x, y + 1, x_limit, y_limit)
##    하단 체크
    if y - 1 >= 0:
        if ar[x][y - 1] == 1:
            
            ar[x][y - 1] = 0
            check_neighbor(x, y - 1, x_limit, y_limit)
    return

import sys
sys.setrecursionlimit(10**6) # 재귀에 의한 에러 방지

T = int(sys.stdin.readline())

for i in range(T):
    M, N, K = map(int, sys.stdin.readline().split())

    ar = [[0] * M for i in range(N)]
    
    for j in range(K):
        a, b = map(int, sys.stdin.readline().split())
        ar[b][a] = 1
    cnt = 0

##    이중 반복문의 작동 매커니즘 조심할 것
##    이중 반복문이 각 행을 먼저 고려함을 조심
    for j in range(N):
        for k in range(M):

            if ar[j][k] == 1:

                cnt += 1
                check_neighbor(j, k, N, M)

    print(cnt)
