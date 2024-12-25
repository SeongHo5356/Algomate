import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int, input().split()))

ans = [0]*n

def check_see(i,j):
    for k in range(i+1, j):
        if (l[j]-l[i]) / (j-i) * (k-i) <= l[k] - l[i]:
            return False
    return True

for i in range(n):
    for j in range(i+1, n):
        if check_see(i,j):
            ans[i] += 1
            ans[j] += 1
        
print(max(ans))

