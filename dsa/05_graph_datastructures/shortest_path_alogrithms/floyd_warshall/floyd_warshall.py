"""입력값 받기 및 객체 준비"""

INF = int(1e9) # 무한대 초기화

n = int(input()) # 노드의 개수
m = int(input()) # 간선의 개수

# 2차원 리스트를 만들고 모든 값을 무한으로 초기화
graph = [[INF]*(n+1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용을 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 받아 그 값으로 초기화
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

"""플로이드 마샬 알고리즘 구현"""

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

"""결과 출력"""
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print('infinity', end= ' ')
        else:
            print(graph[a][b], end=' ')
    print()
