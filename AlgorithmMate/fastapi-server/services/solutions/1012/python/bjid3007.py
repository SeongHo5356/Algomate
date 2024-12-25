import sys
input = sys.stdin.readline

dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]
def replaceZero(arr, h, w, y, x):
    nextNode = [[y, x]]
    arr[y][x] = 0
    while nextNode:
        y, x = nextNode.pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if nx >= w or ny >= h or nx < 0 or ny < 0:
                continue
            if arr[ny][nx] == 1:
                arr[ny][nx] = 0
                nextNode.append([ny, nx])
    return 0


n = int(input())
for _ in range(n):
    # 입력
    w, h, k = map(int, input().split())
    arr = [[0] * w for _ in range(h)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    #
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j]:
                replaceZero(arr, h, w, i, j)
                cnt += 1
    
    print(cnt)