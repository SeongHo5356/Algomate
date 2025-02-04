import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
visit = []
CABBAGE = 0
result = []

def Ground(a, b, c):
    g = list("0"*a)
    ground = list(g[:] for _ in range(b))
    for _ in range(c):
        y, x = map(int, input().split())
        ground[x][y] = '1'
    return ground

def Check(ground, visit, x, y, A, B):

    if x - 1 >= 0 and ground[x-1][y] == '1': # 위
        visit.append([x-1, y])
        ground[x-1][y] = '0'
    if y - 1 >= 0 and ground[x][y-1] == '1': # 왼쪽
        visit.append([x, y-1])
        ground[x][y-1] = '0'
    if x + 1 < B and ground[x+1][y] == '1': # 아래
        visit.append([x+1, y])
        ground[x+1][y] = '0'
    if y+1 < A and ground[x][y+1] == '1': # 오른쪽
        visit.append([x, y+1])
        ground[x][y+1] = '0'

    if len(visit) != 0: # 방문할 곳이 있다면
        x = visit[0][0]
        y = visit[0][1]
        visit.pop(0)
        Check(ground, visit, x, y, A, B) # 거기에서 방문해..


for i in range(int(input())):
    A, B, C = map(int, input().split())
    ground = Ground(A, B, C)
    CABBAGE = 0
    for i in range(A):
        for j in range(B):
            if ground[j][i] == '1':
                CABBAGE += 1
                visit.append([j, i])
                ground[j][i] = '0'
                visit.pop()
                Check(ground, visit, j, i, A, B)
    result.append(CABBAGE)

for i in result:
    print(i)