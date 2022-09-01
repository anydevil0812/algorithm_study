# aXb 형태로 숫자 카드들을 나열하고 각 행마다 가장 작은 수 중에서 가장 큰 수 구하기

a, b = map(int, input().split())
li = []
for i in range(a):
    card = list(map(int, input().split()))
    small = min(card)
    li.append(small)
print(max(li))
