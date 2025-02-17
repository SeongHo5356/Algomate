import sys

n = int(input())
result = list(sys.stdin.readline().strip())
for i in range(n-1): 
    input = list(sys.stdin.readline().strip())
    for j in range(len(result)): 
        if result[j] != input[j]: 
            result[j] = "?"
print("".join(map(str,result)))