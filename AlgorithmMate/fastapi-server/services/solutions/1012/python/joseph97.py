def mod(y,x):
    temp = [(y,x)]
    while temp:
        y ,x = temp.pop()
        for i in range(4):
            Y = y  + dy[i]
            X = x + dx[i]
            if 0 <= Y < N and 0 <= X < M and A[Y][X]:
                A[Y][X] = 0
                temp.append((Y,X))

p = open(0)
dy = [-1,1,0,0]
dx = [0,0,-1,1]

for _ in range(int(next(p))):
    M,N,K = map(int,next(p).split())
    A = [[0]*M for _ in range(N)]
    for _ in range(K):
        X,Y = map(int,next(p).split())
        A[Y][X] = 1
    c = 0
    for a in range(N):
        for b in range(M):
            if A[a][b]:
                A[a][b] = 0
                c += 1
                mod(a,b)
                
    print(c)