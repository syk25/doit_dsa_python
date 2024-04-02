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