# 주어진 돈을 거슬러 줄때 가능한 동전의 최소 개수

a = int(input())
count = 0
b = [500, 100, 50, 10]
for i in b:
    count += a // i
    a %= i
print(count)