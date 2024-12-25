#재귀 이용
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(x,y):
    if x<=-1 or x>=length or y<=-1 or y>=width:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
for _ in range(int(input())):
    width, length, num = map(int, input().split())
    graph = [[0 for _ in range(width)] for _ in range(length)]
    for _ in range(num):
        a, b = map(int, input().split())
        graph[b][a] = 1

    result = 0
    for i in range(length):
        for j in range(width):
            if graph[i][j] == 1:
                if dfs(i, j) == True:
                    result += 1

    print(result)