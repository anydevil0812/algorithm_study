# 8X8 체스판에서 지정한 위치에서 나이트가 이동할 수 있는 경우의 수 구하기
dic = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
location = input()
count = 0
method = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]

for i in range(len(method)):
    x = dic.get(location[0])
    y = int(location[1])
    x += method[i][0]
    y += method[i][1]
    if (0 < x < 9) and (0 < y < 9):
        count += 1

print(count)