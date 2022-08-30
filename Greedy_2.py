# a = 리스트 원소의 갯수, b = 몇개의 숫자를 더할건지, c = 같은 숫자가 연속으로 몇번 나올수 있는지
# 합이 가장 크게 나올 수 있도록 코드 짜기
a, b, c = map(int, input().split(' '))
li = list(map(int, input().split(' ')))
li.sort()
first = li[a-1]
second = li[a-2]
count = int(b/(c+1)) * c
count += b % (c+1)

result = 0
result += count * first
result += (b - count) * second

print(result)
