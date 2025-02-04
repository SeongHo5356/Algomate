from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)

def check(x,y):
    global b
    for i in [1,-1]:
        if (x+i,y) in l:
            l.remove((x+i,y))
            check(x+i,y)
        if (x,y+i) in l:
            l.remove((x,y+i))
            check(x,y+i)

        
T = int(stdin.readline())

for _ in range(T):
    M, N, K = map(int, stdin.readline().split())
    l = set()
    lq = []
    b = 0
    for i in range(K):
        a = tuple(map(int,stdin.readline().split()))
        l.add(a)

    while l:
        b+=1
        a = l.pop()
        check(a[0],a[1])
    print(b)
