import sys
from collections import deque

def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	map_apt = [list(map(int,list(readl().strip()))) for r in range(N)]
	return N, map_apt

def FF(r, c):
	d = ((1,0),(0,1),(-1,0),(0,-1))
	q = deque()
	map_apt[r][c] = 0
	q.append((r,c))
	size = 1

	while q:
		r, c = q.popleft()
		for dr, dc in d:
			nr, nc = r + dr, c + dc
			if not 0 <= nr <= N-1: continue
			if not 0 <= nc <= N-1: continue
			if not map_apt[nr][nc]: continue
			
			map_apt[nr][nc] = 0
			q.append((nr,nc))
			size += 1
	return size

def Solve():
	result = []
	for r in range(N):
		for c in range(N):
			if map_apt[r][c]:
				result.append(FF(r,c))
	result.sort()

	return len(result), result

list_size = []

N, map_apt = Input_Data()

cnt, list_size = Solve()

print(cnt)
print(*list_size,sep='\n')
