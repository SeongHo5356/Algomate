import sys
sys.setrecursionlimit(10000)

def worm(x,y):
    graph[x][y] = 2
    if y < m-1 and graph[x][y+1] == 1  :
        worm(x,y+1)
    if y > 0 and graph[x][y-1] == 1:
        worm(x,y-1)
    if x < n-1 and graph[x+1][y] == 1  :
        worm(x+1,y)
    if x > 0 and graph[x-1][y] == 1  :
        worm(x-1,y)
    
t = int(input())
for _ in range(t):
    m,n,k = map(int,sys.stdin.readline().split())
    graph = [[0]*m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        a,b = sys.stdin.readline().split()
        a = int(a)
        b = int(b)
        graph[b][a] = 1
    for i in range(n):
        while 1 in graph[i]:
            worm(i,graph[i].index(1))
            cnt +=1
    print(cnt)