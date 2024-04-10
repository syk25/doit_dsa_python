import sys

input = sys.stdin.readline

length, height = map(int, input().split())

cases = int(input())

vertical = [0, height]
horizon = [0, length]

for i in range(cases):
    x,y = map(int, input().split())
    if x == 0:
        vertical.append(y)
    else:
        horizon.append(y)

vertical.sort()
horizon.sort()

area_max = 0

for i in range(1, len(vertical)):
    for j in range(1, len(horizon)):
        area = (vertical[i] - vertical[i - 1]) * (horizon[j] - horizon[j-1])
        area_max = max(area, area_max)


print(area_max)
