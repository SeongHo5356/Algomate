import sys

input = sys.stdin.readline

T = int(input())

def bfs(x, y, nodes):

    global visits
    
    q = [(y, x)]
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    cnt = 1
    while q:
        ey, ex = q.pop(0)
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]

            if 0 <= nx < M and 0 <= ny < N:

                if nodes[ny][nx] == 1 and visits[ny][nx] == False:
                    visits[ny][nx] = True
                    q.append((ny, nx))
                    cnt += 1
    return cnt

for _ in range(T):
    M, N, K = map(int, input().split(" "))
    nodes = [[0] * M for _ in range(N)]
 
    for k in range(K):
        ind1, ind2 = map(int, input().split(" "))
        nodes[ind2][ind1] = 1




    visits = [[False] * M for _ in range(N)]
    cnt = []
    for y in range(N):
        for x in range(M):
            if nodes[y][x] == 1 and visits[y][x] == False:
                visits[y][x] = True
                f = bfs(x, y, nodes)
                cnt.append(f)

    print(len(cnt))


