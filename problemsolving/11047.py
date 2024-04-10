# 동전의 수 문제

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

coins = []

for _ in range(N):
    coins.append(int(input().strip()))

coins.sort(reverse=True)

count = 0
i = 0
while K > 0:
    if K >= coins[i]: # 주의할 부분! 조건식: 등호
        count = count + K // coins[i]
        K %= coins[i]
    i += 1

print(count)