import sys
input=sys.stdin.readline

dx=[-1,1,0,0] #상하좌우
dy=[0,0,-1,1]

def bfs():
    while len(queue)!=0:
        x,y=queue.pop(0)

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<= nx < m and 0 <= ny < n:
                if matrix[nx][ny] == 1: #지렁이가 이동 가능하면
                    matrix[nx][ny]=0
                    queue.append([nx,ny])

T=int(input())
for _ in range(T):
    m,n,k=map(int,input().split())
    matrix=[[0 for _ in range(n)]for _ in range(m)]

    #배추 행렬 만들기
    for _ in range(k):
        x,y=map(int,input().split())
        matrix[x][y]=1
    
    queue=[]
    count=0
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==1:
                matrix[i][j]=0
                queue.append([i,j])
                bfs()
                count+=1
    print(count)
