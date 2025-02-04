import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

def dfs(graph, i, j, m_num, n_num) :
    graph[i][j] = "Visited"
    if j + 1 <= n_num - 1 and graph[i][j+1] == "Unvisited" :
            dfs(graph, i, j+1, m_num, n_num)
    if i + 1 <= m_num - 1 and graph[i + 1][j] == "Unvisited" :
        dfs(graph, i+1, j, m_num, n_num)
    if j - 1 >= 0 and graph[i][j-1] == "Unvisited" :
        dfs(graph, i, j-1, m_num, n_num)
    if i - 1 >= 0 and graph[i-1][j] == "Unvisited" :
        dfs(graph, i-1, j, m_num, n_num)

def main() :
    t_num = int(input())
    for i in range(t_num) :
        graph, count = [], 0
        m_num, n_num, c_num = map(int, sys.stdin.readline().split())
        for i in range(m_num) :
            graph.append([])
            for j in range(n_num) :
                graph[i].append("Nothing")
        for i in range(c_num) :
            x_num, y_num = map(int, sys.stdin.readline().split())
            graph[x_num][y_num] = "Unvisited"
        for i in range(m_num) :
            for j in range(n_num) :
                if graph[i][j] == "Unvisited" :
                    count += 1
                    dfs(graph, i, j, m_num, n_num)
        print(count)

main()
        

    
