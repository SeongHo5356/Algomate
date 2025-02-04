import sys



def main(M,N,map) :
    cnt = 0
    for i in range(M) :
        for j in range(N) :
            
            if visited[i][j] == 0 and map[i][j] == 1:
                bfs(i,j,N,M)
                cnt +=1
    return cnt
def bfs(i,j,N,M) :
    global visited
    queue = [(i,j)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    while queue :
        x,y =queue.pop(0)
        
        for xx,yy in zip(dx,dy) :
            nx = x+xx 
            ny = y+yy       
            if 0<=nx<M and 0<=ny<N :
                if visited[nx][ny] == 0 and map2[nx][ny] :
                    queue.append((nx,ny)) 
                    visited[nx][ny] = 1
    return visited
readl = sys.stdin.readline
                    
T = int(readl())
                      
for i in range(T) :
    
    M, N, K = map(int, readl().split())
    info = []
    for _ in range(K):
        info.append(list(map(int, readl().split())))

    visited = [[0]*(N) for _ in range(M)]
    map2 = [[0]*(N) for _ in range(M)]
    for y,x in info :
        map2[y][x] = 1
    print(main(M,N,map2))


