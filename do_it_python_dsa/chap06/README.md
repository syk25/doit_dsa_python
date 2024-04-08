## 정렬이란?
**정렬**이란 키(key)들을 <u>항목값의 대소관계</u>에 따라 데이터집합을 일정한 순서로 늘어놓는 작업입니다. 정렬은 데이터를 정렬하면 <u>데이터를 더욱 쉽게 검색</u> 할 수 있습니다. 정렬의 형태로 오름차순 정렬과 내림차순 정렬이 있습니다. **오름차순 정렬**은 <u>값이 작은 데이터부터</u> 앞에 배치합니다. 반대로 **내림차순 정렬**은 <u>값이 큰 데이터부터</u> 앞에 배치합니다.

## 버블정렬

### bubble sort

하나의 패스(pass)를 진행할 때마다 양 옆의 원소의 크기를 비교한 후 교환함으로써 이뤄지는 정렬입니다.

### 버블정렬 코드

```python
N = int(input())

my_list = [int(input()) for _ in range(N)]

# my_list 버블정렬
for i in range(N):
    for j in range(N-1, i, -1):
        if my_list[j - 1] > my_list[j]:
            my_list[j-1], my_list[j] = my_list[j], my_list[j-1]

for i in my_list:
    print(i)

```

## 단순 선택 정렬

단순선택정렬은 한 패스(pass)별 맨 앞의 위치와 최솟값을 교환하면서 정렬해나가는 입니다. 하나의 패스란 하나의 스캔·교환 과정입니다. 최솟값을 선택해서 컨테이너의 앞부터 정렬해나간다는 부분에 착안해 선택정렬이라고도 합니다.

### 구현코드

```python
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
```

## 단순삽입정렬

단순삽입정렬은 배열에서 두번째원소부터 끝 원소까지 하나씩 주목하면서 더 앞쪽에 알맞은 위치로 삽입하며 정렬하는 알고리즘입니다.

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/464f9f97-9358-4c41-be47-0e6717ae78a0/d6219b00-e57d-4cec-a1a4-9ed00d3139ea/Untitled.png)

주목할 원소를 저장할 공간 tmp가 필요합니다. tmp에 주목할 원소를 넣습니다. 주목한 원소의 인덱스부터 앞의 인덱스로 하나씩 값을 비교합니다. 비교값이 tmp보다 크면 비교값을 인덱스를 하나 증가시켜서 저장합니다. 비교값이 tmp보다 작다면 tmp를 비교값의 뒤의 인덱스 자리에 저장합니다. 그 다음에 tmp에 새로 주목할 원소를 넣습니다. 이 과정을 반복하면 삽입정렬이 완료됩니다.

```python
# 단순 삽입 정렬 알고리즘 구현하기

from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    """단순삽입정렬"""
    n = len(a)
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j-1] > tmp:
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp
```

단순삽입정렬은 인근 원소 순으로 이동하기 때문에 안정적입니다. 시간복잡도는 O(N^2)입니다.

## 이진삽입정렬

배열의 크기가 커지면 단순삽입정렬을 하기에는 비효율적입니다. 데이터를 비교와 교환하는 비용이 증가하기 때문입니다. 따라서 주목하는 원소가 앞에 정렬 된 배열에서 자신의 위치를 찾을 때 이진검색을 활용하면 시간복잡도가 O(N^2) 에서 O(NlogN)으로 줄어듭니다.

```python
# 단순 삽입 정렬 알고리즘 구현하기

from typing import MutableSequence

def binary_insertion_sort(a: MutableSequence) -> None:
    """단순삽입정렬"""
    n = len(a)
    for i in range(1, n):
        key = a[i]
        pl = 0
        pr = i - 1
        
        while True:
            pc = (pl + pr) // 2
            if a[pc] == key:
                break
            elif a[pc] < key:
                pl = pc + 1
            else:
                pr = pc - 1
            if pl > pr:
                break
        
        pd = pc + 1 if pl < pr else pr + 1
        
        for j in range(i, pd, -1):
            a[j] = a[j - 1]
        a[pd] = key
```

파이썬의 모듈을 사용하면 이진병합정렬을 훨씬 간단하게 구현할 수 있습니다.

```python
from typing import MutableSequence
import bisect

def binary_insertion_sort(a: MutableSequence) -> None:
    """단순삽입정렬"""
    for i in range(1, len(a)):
        bisect.insort(a, a.pop(i),0,i)
```

## 셸 정렬