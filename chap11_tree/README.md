# 트리
## 트리구조

리스트는 데이터에 순서를 메겨 나열하는 자료구조입니다. 반면에 트리는 데이터의 계층관계를 표현하는 자료구조입니다. 트리는 노드와 가지로 구성됩니다. 트리의 가장 최상단 노드를 루트라고 합니다. 트리의 가장 말단 노드를 리프라고 합니다. 노드에서 더 이상 뻗어나갈 가지가 없을 경우 리프노드로 봅니다.

노드 간에 가지로 연결되어 있을 때 아래쪽 노드를 자식 노드, 위쪽 노드를 부모 노드라고 합니다. 부모노드를 공유하는 노드를 형제노드라고 합니다. 어떤 노드가 가지를 따라 위로 만나는 모든 노드를 조상노드라고 합니다. 어떤 노드를 따라 아래로 만나는 모든 노드를 자손노드라고 합니다. 

각 노드가 갖는 자식의 수를 차수라고 합니다. 루트에서 노드가 떨어진 정도를 레벨이라고 합니다. 루트노드의 레벨은 0입니다. 루트에서 가장 멀리 떨어진 리프까지의 거리, 곧 리프노드의 레벨 최대값을 높이라고 합니다.

트리 내에 어떤 노드를 루트노드로 간주하고 그 자손 노드로 구성된 트리를 서브트리라고 합니다. 노드와 가지가 존재하지 않는 노드를 빈트리라고 합니다. 형제 노드 간에 순서가 있는 경우를 순서 트리, 순서가 없는 경우를 무순서 트리라고 합니다. 순서 트리의 경우, 형제의 배치가 바뀌면 다른 트리로 간주하지만 무순서트리는 동일한 트리로 봅니다.

## 순서트리의 검색

순서트리는 2가지 스캔방식이 있습니다. 너비우선탐색과 깊이우선탐색입니다.

### 너비우선탐색(breadth-first search)

루트노드와 가까운 노드부터 탐색하는 방식입니다. 낮은 레벨부터 왼쪽에서 오른쪽으로 검색하고 하나의 레벨을 마치면 다음 레벨로 넘어가 탐색을 시작합니다.

### 깊이우선탐색(depth-first search)

리프에 도달할 때까지 아래쪽으로 탐색하는 방식입니다. 리프에 도달해서 더 이상 검색할 곳이 없으면 일단 부모노드로 돌아가고 그 뒤 다시 자식노드로 내려갑니다.

깊이우선탐색 방식으로 트리를 스캔을 할 경우 부모노드를 최대 3번 지나가게 됩니다(지나가는 것과 방문하는 것은 다른 개념입니다). 왼쪽 자녀 노드, 오른쪽 자녀 노드, 부모 자녀 노드의 방문 순서에 따라 깊이 우선 타색의 종류가 전위순회(부모-왼쪽-오른쪼), 중위순회(왼쪽-부모-오른쪽), 후위순회(왼쪽-오른쪽-부모) 총 3 종류가 있습니다.

전위 순회는 다음의 순서로 트리를 스캔합니다.

```
노드 방문 -> 왼쪽 자식 -> 오른쪽 자식
```

중위 순회는 다음의 순서로 트리를 스캔합니다.

```
왼쪽 자식 -> 노드 방문 -> 오른쪽 자식
```

후위 순회는 다음의 순서로 트리를 스캔합니다.

```
왼쪽 자식 -> 오른쪽 자식 -> 노드 방문
```

## 이진트리(Binary Tree)

노드가 외쪽과 오른쪽 노드만을 자식노드로 갖는 트리를 이진트리라고 합니다. 이진트리는 노드가 자식노드가 둘 다 있을 수도, 1개만 있을 수도, 아예 없을 수도 있습니다. 이진트리는 순서트리입니다. 즉, 왼쪽 자식과 오른쪽 자식을 구분합니다. 왼쪽 자식을 루트로 하는 왼쪽 서브트리, 그반대는 오른쪽 서브트리라고 합니다.

## 완전이진트리(Complete Binary Tree)

루트에서 아래쪽 레벨로 모든 노드가 채워져 있고 레벨 안에서 외쪽 부터 오른쪽으로 노드가 가득찬 이진트리를 완전이진트리라고 합니다. 리프노드가 존재하는 레벨을 제외한 레벨은 모든 노드가 존재합니다. 리프노드 레벨에 한해서 왼쪽에서 오른쪽으로 반드시 끝까지 채우지 않아도 됩니다. 완전이진트리의 최대 높이는 노드의 개수가 N일 때 logN입니다.

## 이진검색트리(Binary Search Tree)

이진검색트리는 이진트리에 노드에 특별한 조건이 존재하는 트리입니다.

```
1. 왼쪽 서브트리노드의 키값은 자신의 노드 키값보다 작아야 합니다.
2. 오른쪽 서브트리노드의 키값은 자신의 노드 키값보다 커야 합니다.
```

이진트리의 특징은 다음과 같습니다.

```
1. 구조가 단순합니다.
2. 중위순회를 통해 노드값을 오름차순으로 얻을 수 있습니다.
3. 이진검색과 비슷한 방식으로 logN 수준으로 검색할 수 있습니다.
4. 노드를 삽입하기 쉽습니다.
```

## 배열로 트리 구현

---

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/464f9f97-9358-4c41-be47-0e6717ae78a0/8ca2e9db-1133-4af4-80df-d4bd7a726896/Untitled.png)

이진트리를 배열로 표현할 수 있습니다. 부모노드와 자식노드는 다음의 인덱스 관계를 갖습니다.

### [배열활용] 부모노드와 자식노드의 인덱스 관계

```
부모노드의 인덱스: n
자식노드의 인덱스: 2*n + 1, 2*n + 2
```

### [배열활용] 부모-자식 노드의 관계 표현

```python
my_tree = ['A','B','C','D','E','F',None,'G']

i = 0

n = len(my_tree)

while i < n:
    if my_tree[i]:
        print(f"Parent: {my_tree[i]}", end=', ')
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and my_tree[left] is not None:
            print(f"Left: {my_tree[left]}", end=', ')
        if  right < n and my_tree[right] is not None:
            print(f"Right: {my_tree[right]}", end=', ')
        print()
    i += 1

```

### [배열활용] 자식노드의 부모노드 찾기

```python
def find_parent(child: Any ,tree: list) -> None:
    child_idx = tree.index(child)
    parent_idx = 0
    if child_idx % 2 == 1:
        parent_idx = (child_idx - 1) // 2
    else:
        parent_idx = (child_idx - 2) // 2
    print(f"Parent of {child}: {tree[parent_idx]}")

```

### [배열활용] 전위순회

```python
def pre_order(tree: Any, i = 0) -> None:
    """트리의 전위순회"""
    if i < len(tree):
        print(tree[i], end = ' ')
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(tree) and tree[left] is not None:
            pre_order(tree, left)
        if right < len(tree) and tree[right] is not None:
            pre_order(tree, right)
```

### [배열활용] 중위순회

```python
def in_order(tree: Any, i = 0) -> None:
    """트리의 중위순회"""
    if i < len(tree):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(tree) and tree[left] is not None:
            in_order(tree, left)
        print(tree[i], end = ' ')
        if right < len(tree) and tree[right] is not None:
            in_order(tree, right)
```

### [배열활용] 후위순회

```python
def post_order(tree: Any, i = 0) -> None:
    """트리의 후위순회"""
    if i < len(tree):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(tree) and tree[left] is not None:
            post_order(tree, left)
        if right < len(tree) and tree[right] is not None:
            post_order(tree, right)
        print(tree[i], end = ' ')
```

## 연결리스트로 구현

---