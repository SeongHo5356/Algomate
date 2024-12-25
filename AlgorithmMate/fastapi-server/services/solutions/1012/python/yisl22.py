#백준 1012

import sys
sys.setrecursionlimit(10**6)

def makezero(x,y) :
    Bat[y][x] = 0
    if y > 0 and Bat[y-1][x] == 1 :
        makezero(x,y-1)
    if y < N-1 and Bat[y+1][x] == 1 :
        makezero(x,y+1)
    if x > 0 and Bat[y][x-1] == 1 :
        makezero(x-1,y)
    if x < M-1 and Bat[y][x+1] == 1 :
        makezero(x+1,y)

T = int(sys.stdin.readline())

for t in range(T) :
    M, N, K = map(int, sys.stdin.readline().split())
    Bat = [[0 for i in range(M)] for j in range(N)]
    for k in range(K) :
        col, row = map(int, sys.stdin.readline().split())
        Bat[row][col] = 1
    count = 0
    for m in range(M) :
        for n in range(N) :
            if Bat[n][m] == 1 :
                count += 1
                makezero(m,n)
    print(count)
