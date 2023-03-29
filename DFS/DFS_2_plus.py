import sys

def Input_Data():
	N, K = map(int, readl().split())
	num = list(map(int, readl().split()))
	return N, K, num

def DFS(n, sum):
	if sum == K: return True
	if sum > K: return False
	if n >= N: return False

	for i in range(n, N):
		if DFS(i+1, sum + num[i]): return True
	return False

def Solve():
	if DFS(0, 0): sol.append("YES")
	else: sol.append("NO")

sol = []

readl = sys.stdin.readline

T = int(readl())
for _ in range(T):
	N, K, num = Input_Data()
	possible = 0
	Solve()	

print(*sol, sep = '\n')
