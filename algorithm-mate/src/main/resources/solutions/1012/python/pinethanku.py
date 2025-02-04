#유기농 배추

import sys

global garo, sero

sys.setrecursionlimit(10**6)  #파이썬의 최대 재귀 깊이를 높임

def search(save, n, m) :
    global garo, sero
    
    save[n][m] = 0
    if m<sero-1 and save[n][m+1] == 1 :  #right
        search(save,n,m+1)
    if m>0 and save[n][m-1] == 1 : #left
        search(save,n,m-1)
    if n<garo-1 and save[n+1][m] == 1 : #down
        search(save,n+1,m)
    if n>0 and save[n-1][m] == 1 : #up
        search(save,n-1,m)
    
    return 0

def baechu_1012():
    global garo, sero
   
    num = int(sys.stdin.readline())
    result = []
    for i in range(num) :
        garo, sero, times = tuple(map(int, sys.stdin.readline().split()))
        save = [[0 for i in range(sero)] for i in range(garo)]
        for i in range(times):
            x, y = tuple(map(int, sys.stdin.readline().split()))
            save[x][y] = 1
            
        if times==1:
            result.append(1)
            continue
        
        sector = 0
        
        for i in range(garo) :
            for k in range(sero) :
                if save[i][k] == 1:
                    sector += 1
                    search(save, i, k)
        result.append(sector)
    
    for re in result:
        print(re)
        
    return 0
    

baechu_1012()