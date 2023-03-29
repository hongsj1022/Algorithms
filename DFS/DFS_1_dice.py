import sys
  
def Input_Data():
    readl = sys.stdin.readline
    N, M = map(int, readl().split())
    return N, M
  
def Dice1(n):
    if n >= N:
        print(*dice)
        return
  
    for i in range(1, 7):
        dice[n] = i
        Dice1(n+1)
  
  
def Dice2(n, s):
    if n>=N:
        print(*dice)
        return
  
    for i in range(s,7):
        dice[n] = i
        Dice2(n+1, i)
  
  
def Dice3(n):
    if n >= N:
        print(*dice)
        return
  
    for i in range(1,7):
        if full[i]: continue
        dice[n] = i
        full[i] = 1
        Dice3(n+1)
        full[i] = 0
  
  
def Solve():
    if M == 1: Dice1(0)
    elif M == 2: Dice2(0, 1)
    elif M == 3: Dice3(0)
  
# 입력 받는 부분
N, M = Input_Data()
  
dice = [0] * N
full = [0] * 7
Solve()
