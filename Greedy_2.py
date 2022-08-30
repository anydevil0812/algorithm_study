# a = 리스트 원소의 갯수, b = 몇개의 숫자를 더할 건지, c = 같은 숫자가 연속으로 몇번 나올수 있는지
# 합이 가장 크게 나올 수 있도록 코드 짜기
a, b, c = map(int, input().split(' '))
li = list(map(int, input().split(' ')))
li.sort()
first = li[a-1] # 가장 큰 수
second = li[a-2] # 두번째로 큰 수
count = int(b/(c+1)) * c # 수열(first b번+second 1번)이 반복되는 횟수
count += b % (c+1) # 가장 큰수가 나올 수 있는 최대 횟수

result = 0
result += count * first
result += (b - count) * second

print(result)
