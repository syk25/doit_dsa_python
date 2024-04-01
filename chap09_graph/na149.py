# 이코테 149p: 음료수 얼려먹기 문제

""" 
input.txt 입력값

4 5
00110
00011
11111
00000
"""


import sys
sys.setrecursionlimit(10**7)

file = open('input.txt', 'r')

N, M = map(int, file.readline().strip().split())

# graph = [[None] * (M + 1)] * (N + 1) # 해당 행은 별도의 객체를 생성하는 것이 아니라 같은 객체의 참조를 여러번 받는다는 의미
graph = [[None] * M for _ in range(N)]

for i in range(0, N):
    line = file.readline().strip().split()[0]
    charactres = [int(x) for x in line]
    for j in range(0, M):
        graph[i][j] = charactres[j]

visited = [[None] * M for _ in range(N)]

print(graph)
count = 0

def dfs(x,y):
    if x <= -1 or x >=N or y <= -1 or y >=M:
        return False
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        dfs(x-1, y)
        dfs(x, y -1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

result = 0

for i in range(N):
    for j in range(M):
        if dfs(i,j) == True:
            result += 1

print(result)
