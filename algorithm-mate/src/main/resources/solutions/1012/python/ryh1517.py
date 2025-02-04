import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

def spray(j,i):
  if ground[i][j]==1:
        ground[i][j]=0
        if i<N-1:
          if ground[i+1][j]==1:
            spray(j,i+1)
            ground[i+1][j]=0 #down
            
        if i>0:
          if ground[i-1][j]==1:
            spray(j,i-1)
            ground[i-1][j]=0 #up
            
        if j>0:
          if ground[i][j-1]==1:
            spray(j-1,i)
            ground[i][j-1]=0 #left
            
        if j<M-1:
          if ground[i][j+1]==1:
            spray(j+1,i)
            ground[i][j+1]=0 #right
            


T=int(input())
for a in range(T):
  M,N,K=map(int,input().split())
  ground=[[0]*M for _ in range(N)]
  for b in range(K):
    x,y=map(int,input().split())
    ground[y][x]=1
  cnt=0

  for i in range(N):
    for j in range(M):
      if ground[i][j]==1:
        spray(j,i)
        cnt+=1

  print(cnt)