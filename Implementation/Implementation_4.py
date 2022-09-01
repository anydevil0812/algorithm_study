a, b = map(int, input().split())
ground = [[0] * b for i in range(a)] # aXb 맵 생성
x, y, d = map(int, input().split())
ground[x][y] = 1
dx = [-1, 0, 1, 0]
dy = []
li =[]
def v():
    
for i in range(a):
    m = list(map(int, input().split()))
    li.append(m)
x += 1
y += 1
for
    if d == 0:
        y += 1
    elif d == 1:
        x += 1
    elif d == 2:
        y -= 1
    elif d == 3:
        x -= 1
