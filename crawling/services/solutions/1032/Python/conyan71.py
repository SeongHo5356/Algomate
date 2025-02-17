n = int(input())
files = [input().strip() for _ in range(n)]

pattern = list(files[0])

for i in range(len(pattern)):
    for j in range(1,n):
        if pattern[i] != files[j][i]:
            pattern[i] =  '?'
            break

print(''.join(pattern))