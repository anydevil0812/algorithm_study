a, b = map(int, input().split())
li = []
for i in range(a):
    card = list(map(int, input().split()))
    small = min(card)
    li.append(small)
print(max(li))
