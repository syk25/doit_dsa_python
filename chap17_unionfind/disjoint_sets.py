# 서로소 집합 알고리즘
""" 
필요함수: 1. find_parent, 2.union_parent
"""
# 필요한 함수 정의하기


def find_parent(parent, a):
    """노드 a의 루트노드를 parent 테이블을 통해 반환"""
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]


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
