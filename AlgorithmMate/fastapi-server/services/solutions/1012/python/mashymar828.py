import sys
sys.setrecursionlimit(10000) # 재귀 깊이 설정

for _ in range(int(sys.stdin.readline())):
  M,N,K=map(int,sys.stdin.readline().split())
  graph=[[0]*M for i in range(N)]
  
  for _ in range(K):
    X,Y= map(int,sys.stdin.readline().split())
    graph[Y][X]=1
  
  def dfs(y,x):
    if x<0 or y<0 or x>=M or y>=N:
      return False
    
    if graph[y][x]==1:
      graph[y][x]=0
      dfs(y-1,x)
      dfs(y,x-1)
      dfs(y+1,x)
      dfs(y,x+1)
      return True
    else:
      return False
  
  count=0
  for i in range(N):
    for j in range(M):
      if dfs(i,j)==True:
        count+=1
  
  print(count)