import sys
  
def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	matrix = [[0] + list(map(int, readl().split())) if 1<=n<=N else [0]*(N+1) for n in range(N+1)]
	
	return N, matrix
  
  
def DFS(cnt, city, sum):
	global sol
	if sol <= sum: return
	if cnt == N:
		if matrix[city][1]:
			if sol > sum + matrix[city][1]:
				sol = sum + matrix[city][1]
		return
  
	for n in range(2, N+1):
		if chk[n]: continue
		if not matrix[city][n]: continue
		chk[n] = 1
		DFS(cnt + 1, n, sum + matrix[city][n])
		chk[n] = 0
  
N, matrix = Input_Data()

sol = 999999
chk = [0] * (N+1)

DFS(1, 1, 0)
  
print(sol)
