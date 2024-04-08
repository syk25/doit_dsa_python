# 고정길이 스택 클래스 구현하기

from typing import Any

class FixedStack:
    """고정 길이 스택 클래스"""
    class Empty(Exception):
        """비어있는 fixedstack에 pop, peek를 할 경우 예외처리"""
        pass
    
    class Full(Exception):
        """가득찬 fixedstack에 push를 할 경우 예외처리"""
        pass
    
    def __init__(self, capacity: int = 256) -> None:
        """스택 초기화"""
        self.stk = [None] * capacity
        self.capacity = capacity
        self.ptr = 0
    
    def __len__(self)-> int:
        """스택에 쌓여있는 데이터의 수 반환"""
        return self.ptr
    
    def is_empty(self) -> bool:
        """스택이 비어있는지 판단"""
        return self.ptr <= 0 # 부등호를 통해 오류 회피
    
    def is_full(self) -> bool:
        """스택이 가득 찼는지 판단"""
        return self.ptr >= self.capacity # 부등호를 통해 오류 회피
    
    def push(self, value: Any) -> None:
        """스택에 value를 푸시(데이터를 넣음)"""
        if self.is_full():
            raise FixedStack.Full
        self.stk[self.ptr] = value
        self.ptr += 1
    
    def pop(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        self.ptr -= 1
        return self.stk[self.ptr]
    
    def peek(self) -> Any:
        if self.is_empty():
            raise FixedStack.Empty
        return self.stk[self.ptr-1]
    
    def clear(self) -> None:
        """스택을 비움: 모든 데이터 제거"""
        self.ptr = 0
    
    def find(self, value:Any) -> Any:
        """스택에서 데이터를 검색"""
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i    # 검색성공
        return -1   # 검색실패
    
    def count(self, value) -> int:
        """특정 데이터의 개수를 반환"""
        count = 0
        for i in  range(self.ptr -1, -1, -1):
            if self.stk[i] == value:
                count += 1
        return count
    
    def __contains__(self, value:Any) -> bool:
        for i in range(self.ptr -1, -1, -1):
            if self.stk[i] == value:
                return True
        return False

    def dump(self) -> None:
        """바닥부터 꼭대기까지의 순으로 데이터 출력"""
        if self.is_empty():
            print('스택이 비어있습니다.')
        print(self.stk[:self.ptr])
        