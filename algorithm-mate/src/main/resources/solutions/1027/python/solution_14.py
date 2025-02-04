def CCW(i,j,k):
  return (i*A[j]+j*A[k]+k*A[i])-(A[i]*j+A[j]*k+A[k]*i)

N=int(input())
A=[*map(int,input().split())]
CNT=[0]*N
for i in range(N):
  for j in range(i+1,N):
    ok=1
    for k in range(i+1,j):
      if CCW(i,j,k)>=0:ok=0;break
    if ok:CNT[i]+=1; CNT[j]+=1
print(max(CNT))