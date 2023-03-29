import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N, M = map(int, readl().split())
	R, C, S, K = map(int, readl().split())
	return N, M, R, C, S, K

def BFS():
	q = deque()
	d = ((-2, 1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1))
	chk = [[0] * (M+2) for r in range(N+2)] #check list

	q.append((R,C,0))
	chk[R][C] = 1
	
	while q:
		r, c, t = q.popleft()
		for dr, dc in d:
			nr, nc, nt = r + dr, c + dc, t + 1
			if not 1 <= nr <= N: continue
			if not 1 <= nc <= M: continue
			if chk[nr][nc] == 1: continue
			if nr == S and nc == K: return nt
			q.append((nr, nc, nt))
			chk[nr][nc] = 1
			
	return -1
		
N, M, R, C, S, K = Input_Data()

sol = BFS()

print(sol)
