# NxM 크기 얼음 틀 (구멍=0, 칸막이=1) 구멍이 뚫려 있는 부분끼리 상하좌우가 붙어 있으면 서로 연결되어 있는 것
# N,M이 주어질 때 생성 되는 아이스크림의 개수 구하기 (뭉쳐 있는 것의 개수)
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    if x < 0 or x > n-1 or y < 0 or y > m-1:
        return False
    if graph[x][y] == 0:
        graph[x][y] = True
        dfs(x+1, y)
        dfs(x-1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return 'finish'
    return False

count = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == 'finish':
            count += 1
print(count)
