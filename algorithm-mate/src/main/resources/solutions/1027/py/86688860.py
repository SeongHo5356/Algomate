N = int(input())
arr = list(map(int, input().split()))

max_count = 0

for i in range(N):
    cnt = 0

    # 왼쪽 방향
    left_slope = float('inf')  # 초기값을 +inf로 설정 (기울기가 작아야 보임)
    for j in range(i - 1, -1, -1):
        slope = (arr[i] - arr[j]) / (i - j)  # 기울기 계산
        if slope < left_slope:  # 현재 기울기가 더 작다면 보임
            cnt += 1
            left_slope = slope  # 최소 기울기 갱신

    # 오른쪽 방향
    right_slope = float('-inf')  # 초기값을 -inf로 설정 (기울기가 커야 보임)
    for j in range(i + 1, N):
        slope = (arr[j] - arr[i]) / (j - i)  # 기울기 계산
        if slope > right_slope:  # 현재 기울기가 더 크다면 보임
            cnt += 1
            right_slope = slope  # 최대 기울기 갱신

    # 최대값 갱신
    max_count = max(max_count, cnt)

print(max_count)
