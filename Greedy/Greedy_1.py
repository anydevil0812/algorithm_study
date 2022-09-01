a = int(input())
count = 0
b = [500, 100, 50, 10]
for i in b:
    count += a // i
    a %= i
print(count)