# 큐

## 개론
### 큐란?
큐는 스택과 같이 데이터를 임시로 저장하는 자료구조 입니다. 스택은 가장 나중에 들어간 데이터가 먼저 나오는 후입선출(Last in First Out, LIFO) 구조라면 큐는 가장 먼저 들어간 데이터가 먼저 나오는 선입선출(First in First Out, FIFO) 구조 입니다. 은행창구에서 번호표대로 업무 보는 사람들, 놀이기구를 타기 위해 줄을 사는 사람들 모두 큐입니다.

### 큐의 작업와 구조
큐에 데이터를 넣는 행위를 인큐(enqueue)라고 합니다. 데이터를 제거하는 행위를 디큐(dequeue)라고 합니다. 큐에서 데이터 입구는 rear, 데이터 출구는 front 라고 합니다.

### 큐의 구현방법
큐는 배열로 구현하는 방법과 링 버퍼로 구현하는 방법 두가지가 있습니다. 큐는 데이터의 추가 · 삭제가 빈번하게 일어나는 구조임을 고려할 때 링 버퍼로 구현하는 것이 좋습니다. 데이터를 추가하는 enqueue의 경우 양 구현의 시간복잡도는 O(1)이나, dequeue는 전자의 경우는 O(N)인 반면 후자는 O(1)이기 때문입니다.

## 링버퍼로 큐 구현하기
### 링버퍼란?
링버퍼란 배열의 맨 끝의 공간과 맨 앞의 공간이 연결되어 있는 자료구조입니다. 맨 앞공간과 맨 끝의 공간은 front, rear 변수를 통해 식별합니다. front와 rear는 논리적인 데이터 순서일뿐, 배열의 물리적인 원소의 순서는 아닙니다.

### 큐 초기화
큐에 5가지 변수를 지정합니다. `no` 는 큐에 쌓여 있는 데이터의 수 입니다. `front`는 큐의 맨 앞의 원소의 인덱스입니다. `rear`는 가장 마지막에 넣은 원소의 인덱스의 다음 인덱스입니다. `capacity`는 큐가 가질 수 있는 최대 원소의 개수입니다. `que`는 큐로서 데이터를 저장하는 list형 배열입니다.

```python
    def __init__(self, capacity:int) -> None:
        """큐 초기화"""
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity
```

### 큐에 현재 있는 데이터의 수 확인

```python
    def __len__(self) -> bool:
        """큐에 있는 모든 데이터의 수를 반환"""
        return self.no
```

### 큐가 비어있는 지 확인

```python
    def is_empty(self) -> bool:
        """큐가 비어있는지를 판단"""
        return self.no <= 0

```

### 큐가 가득 차 있는지 확인

```python
    def is_full(self) -> bool:
        """큐가 차 있는지를 판단"""
        return self.n0 >= self.capacity

```

### enqueue

```python
    def enqueue(self, value:int) -> None:
        """데이터를 인큐"""
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = value
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0
```

### dequeue

```python
    def dequeue(self, value: int) -> int:
        """데이터를 디큐"""
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x

```

### peek

```python
    def peek(self) -> Any:
        """데이터를 피크"""
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]
```

### find
특정 원소가 큐에 있는지를 찾는 함수입니다. 원소가 존재하면 인덱스를 반환하고 없으면 -1을 반환합니다.

```python
    def find(self, value: Any) -> Any:
        """데이터를 찾아 인덱스를 반환"""
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1

```

### __contains__

```python
    def __contains__(self, value: Any) -> bool:
        """큐에 value가 있는 지 판단"""
        return self.count(value)
```

### clear

```python
    def clear(self) -> None:
        """큐의 모든 데이터를 비움"""
        self.no = self.front = self.rear = 0

```

### dump

```python
    def dump(self) -> None:
        """모든 데이터를 맨 앞부터 끝 순으로 출력"""
        if self.is_empty():
            print('큐가 비어 있습니다.')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end = ' ')

```

## 참고문헌