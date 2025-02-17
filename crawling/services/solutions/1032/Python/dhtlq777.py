import sys
input = sys.stdin.readline

n = int(input())
stand = list(input())
length = len(stand)
for _ in range(n - 1):
    curr = input()
    for i in range(length):
        if stand[i] != '?' and curr[i] != stand[i]:
            stand[i] = '?'
print(''.join(stand))