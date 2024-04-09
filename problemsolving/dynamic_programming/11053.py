import sys

input = sys.stdin.readline

N = int(input())
numbers = [x for x in map(int, input().split())]

dpt = [1] * (N)

for i in range(1, N):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dpt[i] = max(dpt[i],dpt[j] + 1)

print(max(dpt))