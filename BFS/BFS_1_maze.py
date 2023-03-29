import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	W, H = map(int, readl().split())
	sw, sh, ew, eh = map(int, readl().split())
	map_maze = [[0] + list(map(int, readl().strip())) + [0] if 1<=h<=H else [0] * (W+2) for h in range(H+2)]
	return W, H, sw, sh, ew, eh, map_maze

def BFS():
	d = ((-1,0), (1,0), (0,-1), (0,1))
	q = deque()
	chk = [[0] * (W+2) for h in range(H+2)] #check list
	
	q.append((sh, sw, 0)) #start position
	chk[sh][sw] = 1
	
	while q:
		h, w, time = q.popleft()
		for dh, dw in d:
			nh, nw, ntime = h+dh, w+dw, time+1
			if nh == eh and nw == ew:
				return ntime

			if not 1 <= nh <= H: continue
			if not 1 <= nw <= W: continue
			if map_maze[nh][nw] == 1: continue
			if chk[nh][nw] == 1: continue

			q.append((nh, nw, ntime))
			chk[nh][nw] = 1
	return -1
	

sol = -1

W, H, sw, sh, ew, eh, map_maze = Input_Data()

sol = BFS()

print(sol)
