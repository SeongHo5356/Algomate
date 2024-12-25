import sys
input=sys.stdin.readline
sys.setrecursionlimit(10000)
def DFS(f, x, y, M, N):
    f[y][x]=False
    if x<M-1 and f[y][x+1]==True: DFS(f, x+1, y, M, N)
    if x>0 and f[y][x-1]==True: DFS(f, x-1, y, M, N)
    if y<N-1 and f[y+1][x]==True: DFS(f, x, y+1, M, N)
    if y>0 and f[y-1][x]==True: DFS(f, x, y-1, M, N)
T=int(input())
for i in range (T):
    M, N, K=map(int, input().split())
    f=[[False]*M for k in range(N)]
    v=[[False]*M for k in range(N)]
    for j in range (K):
        a,b=map(int, input().split())
        f[b][a]=True
    count=0
    for x in range(M):
        for y in range(N):
            if f[y][x]==True: 
                count+=1
                DFS(f, x, y , M, N) 
    print(count)

