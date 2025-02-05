import sys

n=int(sys.stdin.readline().rstrip())
arr=list(map(int,sys.stdin.readline().split()))
max_cnt=0

for i in range(n):
    point=arr[i]
    cnt=0

    max_grad = 0
    for j in range(i+1,n): # point 기준 오른쪽 고층건물
        grad=(arr[j]-arr[i])/(j-i)
        if j==i+1 or max_grad<grad:
            max_grad=grad
            cnt+=1

    max_grad = 0
    for j in range(i-1,-1,-1):  # point 기준 왼쪽 고층건물
        grad = (arr[j] - arr[i]) / (i - j)
        if j==i-1 or max_grad < grad:
            max_grad = grad
            cnt += 1

    if max_cnt<cnt:
        max_cnt=cnt
        
print(max_cnt)