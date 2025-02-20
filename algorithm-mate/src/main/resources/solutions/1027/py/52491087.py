n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    std = arr[i]
    pre_slope = None
    left_cnt = 0
    right_cnt = 0
    for j in range(i-1, -1, -1):
        slope = (std - arr[j]) / (i - j)
        if pre_slope == None or pre_slope > slope:
            pre_slope = slope
            left_cnt += 1
    pre_slope = None
    for k in range(i+1, n):
        slope = (std - arr[k]) / (i - k)
        if pre_slope == None or pre_slope < slope:
            pre_slope = slope
            right_cnt += 1
    if cnt < left_cnt + right_cnt:
        cnt = left_cnt + right_cnt
print(cnt)