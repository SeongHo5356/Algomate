import sys
sys.setrecursionlimit(10**6)

def search(x, y):
    bat[x][y] = 0
    if y+1 <= m-1 and bat[x][y+1] == 1:
        search(x, y+1)
    if x+1 <= n-1 and bat[x+1][y] == 1:
        search(x+1, y)
    if y-1 >= 0 and bat[x][y-1] == 1:
        search(x, y-1)
    if x-1 >=0 and bat[x-1][y] == 1:
        search(x-1, y)
    
tc_num = int(sys.stdin.readline())

for i in range(tc_num):
    m, n, k = map(int, sys.stdin.readline().split())
    bat = [[0 for b in range(m)] for a in range(n)]

    for _ in range(k):
        y, x  = map(int, sys.stdin.readline().split())
        bat[x][y] = 1

    answer = 0
    
    for q in range(n):
        for w in range(m):
            if bat[q][w] == 1:
                search(q, w)
                answer+=1
                
    print(answer)
    

