# Union-Find(합집합 찾기)

## 개념
### 서로소 집합과 자료구조

서로소 집합이란 공통 원소가 없는 집합입니다.
서로소 집합 자료구조란 서로소 부분 집합들로 나눠진 원소들의 데이터를 처리하기 위한 자료구조입니다. 서로소 집합 자료구조는 합치기(union)연산과 찾기(find)연산으로 조작할 수 있습니다.

### 서로소 집합 찾기의 메커니즘

```
1. 노드의 집합을 확인합니다.
2. 부모테이블을 갱신합니다.
3. 부모테이블의 결과를 출력합니다.
```

서로소 찾기 로직을 구현해서 그래프에 적용하면 각 노드에 대해 트리 구조를 활용해 루트 노드를 파악할 수 있습니다. 루트노드가 다르면 서로소 집합입니다. 각 노드에 대해 루트노드 정보를 담은 부모테이블을 갱신하면 그 결과를 통해 서로 다른 집합을 특정 지을 수 있습니다.

## 구현
```python
# 서로소 집합 알고리즘
""" 
필요함수: 1. find_parent, 2.union_parent
"""
# 필요한 함수 정의하기

def find_parent(parent, a):
    """노드 a의 루트노드를 parent 테이블을 통해 반환"""
    if parent[a] != a:
        return find_parent(parent, parent[a])
    return a

def union_parent(parent, a, b):
    """a와 b의 부모노드를 확인한 후 다르면 하나로 통일"""
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

""" 객체 준비 및 입력 받기"""

v, e = map(int, input().split())  # v: 정점의 개수, e: 간선의 개수
parent = [0] * (v + 1)  # 부모 테이블 준비

# 부모테이블에서 노드를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

"""로직 적용"""

# 부모테이블을 기반으로 서로소 집합을 표현하기
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

"""결과 출력"""
# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end="")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")

print()

# 부모테이블의 내용 출력
print("각 원소가 속한 집합: ", end="")
for i in range(1, v + 1):
    print(parent[i], end=" ")

```

### 함수 구현

```python
def find_parent(parent, a):
    """노드 a의 루트노드를 parent 테이블을 통해 반환"""
    if parent[a] != a:
        return find_parent(parent, parent[a])
    return a

def union_parent(parent, a, b):
    """a와 b의 부모노드를 확인한 후 다르면 하나로 통일"""
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
```

### 객체 준비 및 입력 받기

```python
v, e = map(int, input().split())  # v: 정점의 개수, e: 간선의 개수
parent = [0] * (v + 1)  # 부모 테이블 준비

# 부모테이블에서 노드를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i
```

### 로직 수행

```python
"""로직 적용"""

# 부모테이블을 기반으로 서로소 집합을 표현하기
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)
```

### 결과 출력

```python
"""결과 출력"""
# 각 원소가 속한 집합 출력
print("각 원소가 속한 집합: ", end="")
for i in range(1, v + 1):
    print(find_parent(parent, i), end=" ")

print()

# 부모테이블의 내용 출력
print("각 원소가 속한 집합: ", end="")
for i in range(1, v + 1):
    print(parent[i], end=" ")

```

### 경로압축기법

```python
def find_parent(parent, a):
    """노드 a의 루트노드를 parent 테이블을 통해 반환"""
    if parent[a] != a:
		    parent[a] = find_parent(parent, parent[a])
		return parent[a]
```

부모를 찾을 때 부모테이블을 같이 갱신하면 합치기 연산 때 시간복잡도를 줄일 수 있습니다.