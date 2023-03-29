import sys
from collections import deque 
 
def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_nor_pig = [[0] + list(readl()[:-1])+ [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
	return N, map_nor_pig

def FF(r, c, chk):
	d = ((-1,0), (0,-1), (1,0), (0,1))
	q = deque()
	q.append((r,c))
	chk[r][c] = 1
	
	while q:
		r, c = q.popleft()
		for dr, dc in d:
			nr, nc = r + dr, c + dc
			if not 1<=nr<=N: continue
			if not 1<=nc<=N: continue
			if chk[nr][nc]: continue
			if map_nor_pig[nr][nc] != map_nor_pig[r][c]: continue
			q.append((nr,nc))
			chk[nr][nc] = 1
	return chk
	

def Solve_nor():
	chk = [[0] * (N+1) for n in range(N+1)]
	nor_cnt = 0
	for r in range(1, N+1):
		for c in range(1, N+1):
			if not chk[r][c]:
				chk = FF(r,c,chk)
				nor_cnt += 1
	return nor_cnt

def Solve_rg():
	chk = [[0] * (N+1) for n in range(N+1)]
	rg_cnt = 0

	for r in range(1, N+1):
		for c in range(1, N+1):
			if map_nor_pig[r][c] == 'G':
				map_nor_pig[r][c] = 'R'

	for r in range(1, N+1):
		for c in range(1, N+1):
			if not chk[r][c]:
				chk = FF(r,c,chk)
				rg_cnt += 1
	return rg_cnt
	

N, map_nor_pig = Input_Data()

sol_nor_pig, sol_rg_pig = Solve_nor(), Solve_rg()

print(sol_nor_pig, sol_rg_pig)
