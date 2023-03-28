import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	matrix = [[0] + list(map(int, readl().split())) if 1<=s<=N else [0] * (N+1) for s in range(0, N+1)]
	return N, M, matrix

def BFS():
	q = deque()
	chk = [999999] * (N+1)
	prev = [0] * (N+1)
	q.append((1,0))
	chk[1] = 0

	while q:
		n, t = q.popleft()
		if chk[n] < t: continue
		
		for nn in range(1, N+1):
			nt = t + matrix[n][nn]
			if chk[nn] <= nt: continue
			q.append((nn, nt))
			chk[nn] = nt
			prev[nn] = n
	route = []
	r = M
	while r != 1:
		route.append(r)
		r = prev[r]
	route.append(1)
	route = route[::-1]

	return chk[M], route

sol = -1
route = []

N, M, matrix = Input_Data()

sol, route = BFS()

print(sol)
print(*route)
