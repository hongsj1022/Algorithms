import sys

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	matrix = [[0] + list(map(int, readl().split())) if 1<=n<=N else [0] * (N+1)  for n in range(N+1)]
	return N, matrix

def DFS(n, sum):
	global min_cost
	if sum >= min_cost: return
	if n > N:
		min_cost = sum
		return

	for i in range(1, N+1):
		if build[i]: continue
		build[i] = 1
		DFS(n+1, sum + matrix[n][i])
		build[i] = 0

def Solve():
	global min_cost
	min_cost = 10000
	DFS(1, 0)
	return min_cost

N, matrix = Input_Data()

build = [0] * (N+1)
sol = Solve()

print(sol)
