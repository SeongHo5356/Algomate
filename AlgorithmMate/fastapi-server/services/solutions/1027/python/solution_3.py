import sys

def solution():
    N = int(sys.stdin.readline().strip())
    bd = list(map(int, sys.stdin.readline().strip().split()))
    ans = []

    if N <= 3:
        ans.append(N-1)
    else:
        for i, b in enumerate(bd):
            lAns = 0
            rAns = 0

            # 좌측 탐색
            lftSlp = (b - bd[i-1])
            for l in range(i-2, -1, -1):
                if (cSlp := (b - bd[l]) / (i-l)) < lftSlp:
                    lAns += 1
                    lftSlp = cSlp

            if i < N-1:
                # 우측 탐색
                rgtSlp = (bd[i+1] - b)
                for r in range(i+2, N):
                    if (cSlp := (bd[r] - b) / (r-i)) > rgtSlp:
                        rAns += 1
                        rgtSlp = cSlp

            ans.append((lAns+rAns)+2 if 0 < i < N-1 else (lAns+rAns)+1)

    sys.stdout.write(f"{max(ans)}")

solution()