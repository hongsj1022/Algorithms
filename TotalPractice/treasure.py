import sys
from collections import deque 
 
def Input_Data():
	readl = sys.stdin.readline
	R, C = map(int,readl().split())
	map_jewel = [[0] + list(readl()[:-1]) + [0] if 1<=r<=R else [0]*(C+2) for r in range(R+2)]
	return R, C, map_jewel

def BFS(sr, sc):
	chk = [[0] * (C+2) for _ in range(R+2)]
	d = ((1,0), (0,1), (-1,0), (0,-1))
	q = deque()
	q.append((sr,sc,0))
	chk[sr][sc] = 1
	while q:
		r, c, t = q.popleft()
		for dr, dc in d:
			nr, nc, nt = r + dr, c + dc, t+1
			if not 1<=nr<=R: continue
			if not 1<=nc<=C: continue
			if map_jewel[nr][nc] != 'L': continue
			if chk[nr][nc]: continue
			chk[nr][nc] = 1
			q.append((nr,nc,nt))
	return t

def Solve():
	max_dist = 0
	for sr in range(1, R+1):
		for sc in range(1, C+1):
			if map_jewel[sr][sc] == 'L':
				dist = BFS(sr, sc)
				max_dist = max(max_dist, dist)
	return max_dist

R, C, map_jewel = Input_Data()
sol = Solve() 
 
print(sol)
