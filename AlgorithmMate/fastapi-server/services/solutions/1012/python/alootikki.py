import sys
input = lambda : sys.stdin.readline().rstrip()
    
def bfs(a,b):
    curr = [[a,b]]

    while len(curr) > 0:
        to_visit = []
        for x in curr:
            i, j = x
            if grid[i][j] == 1:
                grid[i][j] = 0

                if i > 0 and grid[i-1][j] == 1: to_visit.append([i-1,j])
                if j > 0 and grid[i][j-1] == 1: to_visit.append([i,j-1])
                if i < n-1 and grid[i+1][j] == 1: to_visit.append([i+1,j])
                if j < m-1 and grid[i][j+1] == 1: to_visit.append([i,j+1])

        curr = to_visit

t = int(input())
for _ in range(t):
    m, n, k = map(int,input().split())
    grid = [[0]*m for _ in range(n)]

    for _ in range(k):
        j, i = map(int,input().split())
        grid[i][j] = 1

    ans = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                ans += 1
                bfs(i,j)
    print(ans)