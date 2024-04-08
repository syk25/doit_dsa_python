# 다익스트라 알고리즘

## 개념
### 사용환경

가중치 그래프에서 시작점과 도착점이 주어졌을 때 최단 경로를 찾는 알고리즘

### 원리

방문할 수 있는 노드 중에 가장 비용이 작은 곳(우선순위가 높은 곳)을 방문

```
1. 우선순위 큐에 시작노드 추가
	2. 우선 순위가 가장 높은 노드 추출
	3. 방문 여부 확인
		4. 비용 업데이트
		5. 현재노드와 연결된 노드를 우선순위 큐에 추가
6. 목적지에 기록 된 비용 반환
```

## 구현
### 가중치 그래프

```python

```

### 다익스트라 알고리즘

```python
import heapq

def dijkstra(graph, start, final):
    costs = {}
    pq = []
    heapq.heappush(pq, (0, start))
    
    while pq:
        cur_cost, cur_v = heapq.heappop(pq)
        if cur_v not in costs:
            costs[cur_v] = cur_cost
            for cost, next_v in graph[cur_v]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_v))
    return costs[final]

```

## 예제: 네트워크에서 최소 딜레이 시간 구하기
```python
from collections import defaultdict
from heapq import heapify, heappop, heappush

times = [[2,1,2],[2,3,5],[2,4,1],[4,3,3]]
n = 4
k = 2

# 1. 접근법 설계
# 그래프 구현
# 다익스트라 알고리즘
# 방문 못한 노드 찾기
# 최소값 중에 최대값 찾기

# 2. 시간복잡도 분석
# 각 단계별 소요되는 시간복잡도 계산

def network(times, n, k):
    graph = defaultdict(list)
    for time in times:
        graph[time[0]].append((time[2], time[1]))
    
    costs = {}
    pq = []
    heappush(pq, (0,k))
    
    while pq:
        cur_cost, cur_node = heappop(pq)
        if cur_node not in costs:
            costs[cur_node] = cur_cost
            for cost, next_node in graph[cur_node]:
                next_cost = cur_cost + cost
                heappush(pq, (next_cost, next_node))
        
    for node in range(1, n + 1):
        if node not in costs:
            return -1

    return max(costs.values())
```

## 참고문헌
[코딩테스트 All in one](https://www.inflearn.com/course/%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8-%EC%9E%85%EB%AC%B8-%ED%8C%8C%EC%9D%B4%EC%8D%AC/dashboard)
