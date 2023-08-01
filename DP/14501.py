import sys

readl = sys.stdin.readline

N = int(input())
T, P = [], []

for _ in range(N):
    t, p = map(int, readl().split())
    T.append(t)
    P.append(p)
    
dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if i + T[i] > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[T[i]+i]+P[i])
        
print(dp[0])