import sys
input = sys.stdin.readline

n = int(input())
datas = list(map(int, input().split()))
ans = []
for i in range(n):
  tmp = 0
  left_max = 10 ** 10
  for j in range(i-1, -1, -1):
    if i == j + 1:
      tmp += 1
      if left_max > (datas[i]-datas[j])/(i-j):
        left_max = (datas[i]-datas[j])/(i-j)
    else:
      if left_max > (datas[i]-datas[j])/(i-j):
        left_max = (datas[i]-datas[j])/(i-j)
        tmp += 1
  right_max = -10 ** 10
  for j in range(i+1, n):
    if i == j - 1:
      tmp += 1
      if right_max < (datas[i]-datas[j])/(i-j):
        right_max = (datas[i]-datas[j])/(i-j)
    else:
      if right_max < (datas[i]-datas[j])/(i-j):
        right_max = (datas[i]-datas[j])/(i-j)
        tmp += 1
  ans.append(tmp)

print(max(ans))