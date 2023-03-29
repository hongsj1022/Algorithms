import sys
 
def Input_Data():
	readl = sys.stdin.readline
	N = int(readl())
	A, B = map(int, readl().split())
	S = int(readl())
	seq = [int(readl()) for _ in range(S)]
	return N, A, B, S, seq
 
def DFS(s, left, right, sum_move):
	global sol
	if sol <= sum_move:
        	return
	if s >= S:
        	sol = sum_move
        	return
   
	if seq[s] < right:
        	DFS(s+1, seq[s], right, sum_move + abs(left-seq[s]))
	if left < seq[s]: 
        	DFS(s+1, left, seq[s], sum_move + abs(right-seq[s]))

N, A, B, S, seq = Input_Data()

sol = 999999

DFS(0, min(A,B), max(A,B), 0)
 
print(sol)
