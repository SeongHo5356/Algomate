import sys

sys.setrecursionlimit(10000)

T = int(sys.stdin.readline().strip())

def dfs(arr,r,c,color,M,N):
    arr[r][c] = color
    if r!=0 and arr[r-1][c] == 1:
        dfs(arr,r-1,c,color,M,N)
    if c!=N-1 and arr[r][c+1] == 1:
        dfs(arr,r,c+1,color,M,N)
    if r!=M-1 and arr[r+1][c] == 1:
        dfs(arr,r+1,c,color,M,N)
    if c!=0 and arr[r][c-1] == 1:
        dfs(arr,r,c-1,color,M,N)


for i in range(T):
    M,N,K = map(int,sys.stdin.readline().split())

    arr = [[0 for _ in range(N)] for _ in range(M)]
    for j in range(K):
        r,c = map(int,sys.stdin.readline().split())
        arr[r][c] = 1
    color = 2
    for j in range(M):
        for k in range(N):
            if arr[j][k] == 1:
                dfs(arr,j,k,color,M,N)
                color += 1
    sys.stdout.write(str(color-2)+"\n")
