# 고정길이 큐 클래스

from typing import Any
class FixedQueue:
    
    class Empty(Exception):
        """비어있는 FixedQueue에서 디큐 또는 피크할 때 내보내는 예외처리"""
        pass
    
    class Full(Exception):
        """가득 차 있는 FixedQueue에서 푸시할 때 내보내는 예외처리"""
        pass
    
    def __init__(self, capacity:int) -> None:
        """큐 초기화"""
        self.no = 0
        self.front = 0
        self.rear = 0
        self.capacity = capacity
        self.que = [None] * capacity
    
    def __len__(self) -> bool:
        """큐에 있는 모든 데이터의 수를 반환"""
        return self.no
    
    def is_empty(self) -> bool:
        """큐가 비어있는지를 판단"""
        return self.no <= 0
    
    def is_full(self) -> bool:
        """큐가 차 있는지를 판단"""
        return self.no >= self.capacity
    
    def enqueue(self, value:Any) -> None:
        """데이터를 인큐"""
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = value
        self.rear += 1
        self.no += 1
        if self.rear == self.capacity:
            self.rear = 0
    
    def dequeue(self) -> Any:
        """데이터를 디큐"""
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1
        self.no -= 1
        if self.front == self.capacity:
            self.front = 0
        return x
        
    def peek(self) -> Any:
        """데이터를 피크"""
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]
        
        
    def find(self, value: Any) -> Any:
        """데이터를 찾아 인덱스를 반환"""
        for i in range(self.no):
            idx = (i + self.front) % self.capacity
            if self.que[idx] == value:
                return idx
        return -1
    
    def count(self, value: Any) -> int:
        """특정 데이터의 개수를 반환"""
        my_count = 0
        for i in range(self.no):
            if value == self.que[(self.front + i) % self.capacity]:
                my_count += 1
        return my_count
    
    def __contains__(self, value: Any) -> bool:
        """큐에 value가 있는 지 판단"""
        return self.count(value)
    
    def clear(self) -> None:
        """큐의 모든 데이터를 비움"""
        self.no = self.front = self.rear = 0
    
    def dump(self) -> None:
        """모든 데이터를 맨 앞부터 끝 순으로 출력"""
        if self.is_empty():
            print('큐가 비어 있습니다.')
        else:
            for i in range(self.no):
                print(self.que[(i + self.front) % self.capacity], end = ' ')
                