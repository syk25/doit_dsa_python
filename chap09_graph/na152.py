from collections import deque

""" input.txt: 이코테(152p)
5 6
101010
111111
000001
111111
111111

"""

file = open('input.txt', 'r')

N, M = map(int, file.readline().strip().split())

graph = [[None] * M for _ in range(N)]

for i in range(N):
    line = file.readline().strip().split()[0]
    for j in range(M):
            graph[i][j] = int(line[j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    
    return graph[N-1][M-1]

print(bfs(0,0))


""" 문제 분석
1. 나의 접근법
길을 하나하나 찾으려고 했다. 하나의 해답을 찾기 위해 하나의 특정한 알고리즘만 선택했다.

2. 정답의 접근법
모든 지점에 대해 거리를 구한 후에 특정 지점에서 거리를 반환했다.
"""