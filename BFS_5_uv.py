import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_uv = [[0] + list(map(int, readl().strip())) + [0] if 1<=r<=N else [0] * (N+2) for r in range(N+2)]
	return N, map_uv

def BFS():
	q = deque()
	d = ((-1,0), (0,-1), (1,0), (0,1))
	chk = [[10000]*(N+2) for w in range(N+2)]
	q.append((1,1, map_uv[1][1]))
	chk[1][1] = map_uv[1][1]
		
	while q:
		h, w, uv = q.popleft()
		if chk[h][w] < uv: continue
		for dh, dw in d:
			nh, nw = h+dh, w+dw
			nuv = uv + map_uv[h][w]
			if not 1<=nh<=N: continue
			if not 1<=nw<=N: continue
			if nuv >= chk[nh][nw]: continue

			q.append((nh, nw, nuv))
			chk[nh][nw] = nuv
								
	return chk[N][N]

N, map_uv = Input_Data()

sol = BFS()

print(sol)
