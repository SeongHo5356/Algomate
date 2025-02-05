import sys

# sys.stdin = open("input.txt")
input = sys.stdin.readline

def solution():
    N = int(input())
    heights = list(map(int, input().split()))
    ans = 0

    for idx, height in enumerate(heights):
        cnt = 0
        min_grad = float('inf')
        max_grad = -float("inf")

        # 왼쪽의 경우
        for i in range(idx - 1, -1, -1):
            c = (heights[i]-height)/(i-idx)
            # 최소 기울기보다 작은 기울기가 나타나면 갱신
            if c < min_grad:
                min_grad = c
                cnt += 1
        # 오른쪽
        for i in range(idx + 1, N):
            c = (heights[i]-height)/(i-idx)
            # 최대 기울기보다 큰 기울기가 나타나면 갱신
            if c > max_grad:
                max_grad = c
                cnt += 1

        ans = max(ans, cnt)
    print(ans)

if __name__ =="__main__":
    solution()