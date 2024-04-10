import sys

input = sys.stdin.readline

N = int(input())

numbers = [int(input()) for _ in range(N)]
sorted_numbers = [0] * N


def qsort(data):
    if len(data) <= 1:
        return data
    
    pivot, tail = data[0], data[1:]
    
    left = [x for x in tail if pivot > x]
    right = [x for x in tail if pivot <= x]
    
    return qsort(left) + [pivot] + qsort(right)

for i in qsort(numbers):
    print(i)

