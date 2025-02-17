n = int(input())
arr = [[] for _ in range(n)]
for i in range(n):
    a = input()
    for j in a:
        arr[i].append(j)

l = len(arr[0])
ans = ""

for i in range(l):
    a = arr[0][i]
    same = True 
    for j in range(n):
        if arr[j][i] != a :
            same = 0 
            break 
    if not same:
        ans += "?"
    else:
        ans += a 

print(ans)