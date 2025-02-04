#유기농 배추

#DFS는 너무 재귀를 많이 돌려서 실패함
#BFS로 도전하자..

import sys

input = sys.stdin.read

data = input().splitlines()

T = int(data[0])

nextbaat = 1

# USING BFS
def placeWorm(i, j): 
    # checkbaat[x][y] = 1
    bsfQueue = [(i,j)]

    while len(bsfQueue)!=0:
        node = bsfQueue.pop(0)
        x = node[0]
        y = node[1]
        checkbaat[x][y] = 1

        if x>0 and baat[x-1][y]==1 and checkbaat[x-1][y]==0:
            checkbaat[x-1][y] = 1
            bsfQueue.append((x-1,y))
        if x<(M-1) and baat[x+1][y]==1 and checkbaat[x+1][y]==0:
            checkbaat[x+1][y] = 1
            bsfQueue.append((x+1,y))
        if y>0 and baat[x][y-1]==1 and checkbaat[x][y-1]==0:
            checkbaat[x][y-1] = 1
            bsfQueue.append((x,y-1))
        if y<(N-1) and baat[x][y+1]==1 and checkbaat[x][y+1]==0:
            checkbaat[x][y+1] = 1
            bsfQueue.append((x,y+1))



def checkCabage(M, N, baat):
    numWorm = 0

    for i in range(M):
        for j in range(N):
            if baat[i][j]==1 and checkbaat[i][j]==0:
                # print(str(i)+", "+str(j))
                numWorm += 1
                placeWorm(i, j)

    return numWorm            


for i in range(T):
    M, N, K = map(int, data[nextbaat].split())

    baat = [[0 for j in range(N)] for i in range(M)]

    for j in range(K):
        x, y = map(int, data[nextbaat+j+1].split())
        baat[x][y] = 1

    checkbaat = [[0 for j in range(N)] for i in range(M)]

    numWorm = checkCabage(M, N, baat)

    nextbaat += K+1
    print(numWorm)
