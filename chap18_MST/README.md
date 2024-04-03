# 최소신장트리 문제
## MST 개념
### MST 개념의 유래

같은 기능의 제품일 때 재료가 더 적은 쪽이 가성비가 좋습니다. 회로를 설계할 때도 마찬가지입니다. 핀의 개수가 동일할 때 전선의 길이가 짧은 회로가 더 좋은 회로입니다. 핀을 정점, 전선을 간선이라고 할 때 모든 정점을 연결한 비순환적 그래프 형태를 최소신장트리라고 합니다. 비순환적이기 때문에 트리이고 그래프를 펼치는(span) 형태이기 때문에 신장트리라고 합니다. 간선의 가중치가 최소가 되게끔 트리를 만드는 것이기 때문에 최소신장트리입니다. 

### 최소신장트리란?

그래프에서 모든 노드를 연결할 때 간선들의 가중치의 합이 최소가 되는 트리를 최소신장트리라고 합니다. 간선의 개수는 노드의 개수보다 1개 작습니다.

### 최소신장트리 문제

그래프를 최소신장트리로 펼치는 문제를 최소신장트리 문제라고 합니다. 최소신장트리 문제는 크루스칼 알고리즘(kruskal's algorithm)과 프림 알고리즘(prim's algorithm)으로 해결할 수 있습니다.

### 최소신장트리 문제 해결원리

크루스칼 알고리즘과 프림 알고리즘 모두 동일한 해결원리를 구현한 알고리즘입니다.

```
1: A <- ∅
2: while A does not form a spanning tree
3: 	do find an edge(u, v) that is safe for A
4: 		A <- A ⋃ {(u,v)}
5: return A
```

A를 간선을 담는 컨테이너로 초기화합니다. A는 정점들을 잇는 ‘안전한 간선’들이 모두 추가되기 전까지는 최소신장트리가 되지 않습니다. 따라서 최소신장트리가 되고나면 A를 반환합니다.

## 크루스칼 알고리즘
### 정의

크루스칼 알고리즘은 MST를 찾는 알고리즘 입니다. 노드들을 비순환적으로 최소 비용으로 연결한 트리를 최소신장트리라고 합니다. 크루스칼 알고리즘은 서로소 찾기 알고리즘을 활용하고 있으므로 사전적으로 알고 있어야 합니다.

### 구현

```python
import sys

def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

input = sys.stdin.readline

V, E = map(int, input().split())

parent = [0] * (V + 1)
for i in range(1, V + 1):
    parent[i] = i

edges = []
result = 0

for i in range(E):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)

```

## 참고문헌
[나동빈의 크루스칼 알고리즘](https://www.youtube.com/watch?v=LQ3JHknGy8c&list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz&index=19)
[이것이 취업을 위한 코딩테스트다 파이썬 편](https://m.yes24.com/Goods/Detail/91433923)