"""함수 정의"""

# input = open('input.txt', 'r').readline().rstrip

# 특정 원소가 속한 집합 찾기
def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

# 집합 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

"""입력값 준비"""
# 그래프 정량 정보 받기
v,e = map(int, input().split())
parent = [0] * (v + 1)

# 간선 정보 받기 준비
edges = []
total_cost = 0

for i in range(1, v+1):
    parent[i] = i

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost,a,b))

"""로직 수행"""
# 1. 간선을 비용순으로 정렬
edges.sort()

# 2. 모든 간선에 대해 사이클을 형성하지 않을 경우 그래프에 추가
for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        total_cost += cost

"""결과 출력"""
print(total_cost)
