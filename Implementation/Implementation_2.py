# 0시 0분 0초부터 a시 59분 59초까지의 시각 중에서 3이 하나라도 포함되는 경우의 수
a = int(input())
count = 0
for i in range(a+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)