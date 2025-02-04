import sys
input = sys.stdin.readline

for _ in range(int(input())):
	M, N, K = map(int, input().split())
	
	test_map = [[0]*M for _ in range(N)]
	for _ in range(K):
		i,j =  map(int, input().split())
		test_map[j][i] = 1 # 배추가 있다.
	
	def dfs(px, py, test_map): # 변수이름 이게 맞나?
		stack = [[px,py]]
		dx = [1, -1 , 0 , 0]
		dy = [0, 0, 1, -1]

		while stack:
			cx, cy = stack.pop()
			test_map[cx][cy] = -1
			for move in range(4):
				nx = cx + dx[move]
				ny = cy + dy[move]

				if (0 <= nx < N) and (0 <= ny < M) and test_map[nx][ny] == 1: ##이거 아마 앞에서 터지면끝나나?
					test_map[nx][ny] = -1 # 방문 했음
					stack.append([nx, ny])


	count = 0
	for i in range(N):
		for j in range(M):
			if test_map[i][j] == 1:
				count +=1 
				dfs(i, j,test_map)
			elif test_map[i][j] <= 0:
				test_map[i][j] = -1
	
	print(count)