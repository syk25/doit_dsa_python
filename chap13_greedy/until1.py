import sys

input = open("input.txt", "r").readline

# input = sys.stdin.readline

N, K = map(int, input().split())

min_count = 0

while N > 1:
    if N % K == 0:
        N //= K
        min_count += 1
    else:
        N -= 1
        min_count += 1

print(min_count)