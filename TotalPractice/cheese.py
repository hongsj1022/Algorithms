import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	R, C = map(int, readl().split())
	map_ch = [list(map(int, readl().split())) for _ in range(R)]
	return R, C, map_ch   

def melt():
	for r in range(R):
		for c in range(C):
			if map_ch[r][c] == 2 or map_ch[r][c] == 3:
				map_ch[r][c] = 0

def BFS():
	d = ((1,0),(0,1),(-1,0),(0,-1))
	q = deque()
	cnt = 0

	q.append((0,0))
	map_ch[0][0] = 2
	
	while q:
		r, c = q.popleft()
		for dr, dc in d:
			nr, nc = r + dr, c + dc
			if not 0 <= nr < R: continue
			if not 0 <= nc < C: continue
			if map_ch[nr][nc] == 0:
				map_ch[nr][nc] = 2
				q.append((nr,nc))
			elif map_ch[nr][nc] == 1:
				map_ch[nr][nc] = 3
				cnt += 1
	return cnt

	
def Solve():
	total = 0
	t = 0
	for r in range(R):
		for c in range(C):
			if map_ch[r][c]: total+=1
	while total:
		temp = total
		to_melt = BFS()
		total -= to_melt
		melt()
		t += 1
	return t, temp

R, C, map_ch = Input_Data()

sol_hour, sol_last_cnt_ch = Solve()
 
print(sol_hour, sol_last_cnt_ch, sep='\n')
