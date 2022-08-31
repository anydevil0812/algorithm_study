# N에서 1을 빼거나 N을 K로 나누는 과정을 최소 몇번 반복해야할지 계산
a, b = map(int, input().split())
count = 0
while a != 1:
    if a % b == 0:
        a = a // b
        count += 1
    else:
        a -= 1
        count += 1
print(count)
