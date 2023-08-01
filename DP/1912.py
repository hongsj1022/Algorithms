import sys

N = int(input())
suyul = list(map(int, sys.stdin.readline().split()))
#suyul = list(map(int, input().split()))

dp = [(-1000)*100000]*(N+2) #i개의 연속된 수의 합 중 가장 큰 값을 저장

# for i in range(1,N+1):
#     for j in range(N-i+1):
#         dp[i] = max(sum(suyul[j:j+i-1]), dp[i])

for i in range(N-1):
    dp[i+1] = max(suyul[i], suyul[i] + suyul[i+1])

print(max(dp))