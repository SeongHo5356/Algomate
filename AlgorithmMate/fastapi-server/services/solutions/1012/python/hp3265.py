import sys; input = sys.stdin.readline

def main():
    for _ in range(int(input())):
        m,n,k = map(int,input().split())
        graph = [[0 for _ in range(m+2)] for _ in range(n+2)]
        nodes = set()
        for _ in range(k):
            x,y = map(int,input().split())
            graph[y+1][x+1] = 1
            nodes.add((y+1, x+1))
        count = 0
        while nodes:
            first = nodes.pop()
            q = [first]
            visited = set((first,))
            while True:
                newq = []
                for point in q:
                    r,c = point
                    z1,z2,z3,z4 = (r, c+1), (r+1, c), (r, c-1), (r-1, c)
                    if graph[r][c+1] and z1 not in visited:
                        visited.add(z1); newq.append(z1)
                    if graph[r+1][c] and z2 not in visited:
                        visited.add(z2); newq.append(z2)
                    if graph[r][c-1] and z3 not in visited:
                        visited.add(z3); newq.append(z3)
                    if graph[r-1][c] and z4 not in visited:
                        visited.add(z4); newq.append(z4)
                if not newq:
                    break
                q = newq.copy()
            nodes -= visited
            count += 1
        print(count)

if __name__ == "__main__":
    main()
