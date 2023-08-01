import sys
from collections import deque

def input_data():
	input_size = int(input())
	readl = sys.stdin.readline
	input_s_x, input_s_y = map(int, readl().split())
	input_e_x, input_e_y = map(int, readl().split())
	
	return input_size, input_s_x, input_s_y, input_e_x, input_e_y

def BFS(size, start_x, start_y, end_x, end_y):
	d = ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))
	q = deque()
	chk = [[0] * size for s in range(size)]

	q.append((start_x, start_y, 0))
	chk[start_x][start_y] = 1
	
	while q:
		x, y, cnt = q.popleft()
		for dx, dy in d:
			nx, ny, ncnt = x + dx, y + dy, cnt + 1
			if nx == end_x and ny ==  end_y:
				return ncnt
			if not 0 <= nx < size: continue
			if not 0 <= ny < size: continue
			if chk[nx][ny] == 1: continue
			
			q.append((nx, ny, ncnt))
			chk[nx][ny] = 1
	return -1
	

def Sol():
	n = int(input())
	
	for i in range(n):
		si, st_x, st_y, e_x, e_y = input_data()
		if st_x == e_x and st_y == e_y:
			print(0)
			continue
		result = BFS(si, st_x, st_y, e_x, e_y)
		print(result)

Sol()
