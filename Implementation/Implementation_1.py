# 공간의 크기와 공간의 크기 만큼 이동할 명령을 입력 받았을 경우의 좌표 구하기
size = int(input())
move = list(input().split())
a, b = 1, 1

for i in range(size+1):
    if (move[i] == 'R') and (b < size):
        b += 1
    elif (move[i] == 'L') and (b > 1):
        b -= 1
    elif (move[i] == 'D') and (a < size):
        a += 1
    elif (move[i] == 'U') and (a > 1):
        a -= 1

print(a, b)
