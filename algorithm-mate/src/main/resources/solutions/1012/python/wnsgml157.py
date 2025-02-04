import sys
input = sys.stdin.readline

def mark_group(x, y, m, n, l, visited):
    stack = [(x, y)]
    
    while stack:
        cx, cy = stack.pop()
        if visited[cx][cy]:
            continue
        
        visited[cx][cy] = True

        # 상하좌우 인접한 배추를 스택에 추가
        if cx > 0 and l[cx-1][cy] == 1 and not visited[cx-1][cy]:
            stack.append((cx-1, cy))
        if cx < m-1 and l[cx+1][cy] == 1 and not visited[cx+1][cy]:
            stack.append((cx+1, cy))
        if cy > 0 and l[cx][cy-1] == 1 and not visited[cx][cy-1]:
            stack.append((cx, cy-1))
        if cy < n-1 and l[cx][cy+1] == 1 and not visited[cx][cy+1]:
            stack.append((cx, cy+1))

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    
    l = [[0]*n for _ in range(m)]
    visited = [[False]*n for _ in range(m)]

    for _ in range(k):
        x, y = map(int, input().split())
        l[x][y] = 1

    groups = 0
    for i in range(m):
        for j in range(n):
            if l[i][j] == 1 and not visited[i][j]:  # 배추가 있고 아직 방문하지 않은 경우
                mark_group(i, j, m, n, l, visited)
                groups += 1  # 새로운 그룹을 발견했으므로 그룹 수 증가
                
    print(groups)
