import sys
input = sys.stdin.readline

n = int(input())
l = list(map(int,input().split()))
if n==1:
    print(0)
    exit()
elif n==2:
    print(1)
    exit()

res = [1]+[2]*(n-2)+[1]

for t in range(n):
    for x in [1,-1]:
        q = l[t::x]
        if len(q)>2:
            tany = q[1]-q[0]
            tanx = 1
            for i in range(2,len(q)):
                if tany*i < tanx*(q[i]-q[0]):
                    tany = q[i]-q[0]
                    tanx = i
                    res[t] += 1

print(max(res))