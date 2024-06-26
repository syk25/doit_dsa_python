# 우선순위큐

## 개념
### 정의

우선순위큐는 들어온 데이터의 우선순위에 따라 데이터를 꺼내는 자료구조입니다. 큐는 들어온 순서에 따라 데이터를 꺼내는 반면에 우선순위큐는 우선순위에 따라 데이터를 꺼냅니다.

우선순위 큐는 3가지 방식으로 구현할 수 있습니다. ① 배열 ② 연결리스트 ③ 힙으로 구현할 수 있습니다. 배열과 연결리스트의 경우, 정렬의 유무에 따라 데이터 처리의 시간복잡도가 O(N) ~ O(NlogN)이나 힙의 경우 O(logN)으로 동일합니다. 따라서 우선순위큐는 힙으로 구현합니다.

### 힙 자료구조 구현

힙 자료구조는 완전이진트리의 한 형태로 리프노드를 제외한 모든 노드들이 점유되어 있고 자식노드는 왼쪽부터 채워지는 구조입니다. 

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/464f9f97-9358-4c41-be47-0e6717ae78a0/3944f1ad-7511-48a1-b69d-71e9a455bcfe/Untitled.png)

완전이진트리의 특징은 다음과 같습니다.

```
1. 리프노드를 제외한 모든 레벨에 노드가 존재
2. 레벨이 비어있는 경우, 노드 추가시 해당 레벨을 채움
3. 왼쪽에서 오른쪽 방향으로 노드가 채워짐
```

완전이진트리는 배열 혹은 연결리스트로 구현할 수 있습니다. 데이터 조작의 성능 때문에 리스트보다 배열로 구현하는 것이 좋습니다. 

### 파이썬에서 힙 활용

```python
from heapq import heapify, heappop, heappush

heap = []

a = [3,5,2,1,6,4]

heapify(a) # 리스트a를 힙 자료구조로 만듬

heappush(a, 0) # 힙에 원소 추가

heappop(a) # 힙에서 루트노드 제거
```

힙은 리스트를 활용해서 구현하기 때문에 인덱스를 통해 노드들을 추적합니다. 부모노드와 자식노드는 다음의 인덱스 관계를 가집니다.

```
부모노드의 인덱스: n
자식 노드의 인덱스: 2n + 1, 2n + 2
```

파이썬에서는 배열로 힙을 만들 경우 minheap 이 만들어집니다. maxheap을 만드려면 몇개의 코드를 추가해야합니다.

`**모든 원소에 -1을 곱하는 경우**`

```python
a = [3,5,2,1,6,4]
for i in range(a):
	a[i] = (-1) * a[i] # 모든 원소에 -1을 곱합니다.

heapify(a) # 힙을 만듭니다.

value = (-1) * heappop(a) # 데이터를 꺼낼 때 -1을 다시 곱합니다.

	
```

`**리스트 활용하기**`

```python
from heapq import heapify, heappop, heappush

a = [3,5,2,1,6,4]
a2 = [None] * len(a)

for i in range(len(a)):
	a2[i] = [(-1)*a[i], a[i]]

heapify(a2)

weight, value = heappop(a2) 
value = heappop(a2)[1]
```

리스트 혹은 튜플 형태로 weight, value 쌍을 만들어 컨테이너 리스트에 넣어줍니다. 컨테이너 리스트를 힙으로 만들면 weight 기준으로 완전이진트리 형태가 리스트로 만들어집니다.