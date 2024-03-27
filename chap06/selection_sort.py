from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:
    """단순선택정렬"""
    n = len(a)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    print(a)

selection_sort([3,4,2,3,1])