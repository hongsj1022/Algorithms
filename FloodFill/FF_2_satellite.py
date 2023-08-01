import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_lake = [[0] + list(map(int,list(readl().strip()))) + [0] if 1<=r<=N else [0]*(N+2) for r in range(N+2)]
	return N, map_lake

def FF(r, c):
	d = ((1,0), (0,1), (-1,0), (0,-1), (-1,-1), (-1,1), (1,-1), (1,1))
	q = deque()
	q.append((r,c))
	map_lake[r][c] = 0
	
	while q:
		r, c = q.popleft()
		for dr, dc in d:
			nr, nc = r + dr, c + dc
			if not 1<=nr<=N: continue
			if not 1<=nc<=N: continue
			if not map_lake[nr][nc]: continue
			q.append((nr,nc))
			map_lake[nr][nc] = 0
	return

def Solve():
	cnt = 0
	for r in range(1,N+1):
		for c in range(1,N+1):
			if map_lake[r][c]:
				FF(r, c)
				cnt += 1
	return cnt

N, map_lake = Input_Data()

sol = Solve()

print(sol)
