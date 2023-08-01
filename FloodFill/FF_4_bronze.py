import sys
sys.setrecursionlimit(10**6)

MAXN = 10**4
N = 0
X = [0]*(MAXN+10)
Y = [0]*(MAXN+10)

MAP = [[0]*110 for _ in range(110)]
visited = [[0]*110 for _ in range(110)]

SH, SW, EH, EW = 0, 0, 0, 0
len = 0
dh = [-1, 1, 0, 0]
dw = [0, 0, -1, 1]


def FindArea():
    global SH, SW, EH, EW
    SH, SW, EH, EW = 100, 100, 0, 0
    for i in range(N):
        if SH > Y[i]: SH = Y[i]
        if SW > X[i]: SW = X[i]
        if EH < Y[i]: EH = Y[i]
        if EW < X[i]: EW = X[i]
    SH -= 1
    SW -= 1
    EH += 1
    EW += 1


def FillArea():
    for i in range(N):
        MAP[Y[i]][X[i]] = 1


def InputData():
    global N
    N = int(input())
    for i in range(N):
        X[i], Y[i] = map(int, input().split())


def FloodFill(h, w):
    global len
    if (h < SH) or (h > EH) or (w < SW) or (w > EW):
        return
    if MAP[h][w]:
        len += 1
        return
    if visited[h][w]:
        return
    visited[h][w] = 1
    for i in range(4):
        FloodFill(h+dh[i], w+dw[i])


def Solve():
    global len
    len = 0
    for i in range(110):
        visited[i] = [0]*110
        MAP[i] = [0]*110
    FindArea()
    FillArea()

    FloodFill(SH, SW)
    return len


if __name__ == '__main__':
    ans = -1
    InputData()

    ans = Solve()
    print(ans)
