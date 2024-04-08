# 고정길이 스택 클래스를 deque를 이용해서 구현하기

from typing import Any
from collections import deque

class Stack:
    """고정 길이 스택 클래스"""
    
    def __init__(self, maxlen: int = 256) -> None:
        self.maxlen = maxlen
        self.__stk = deque([], maxlen)
    
    def __len__(self) -> int:
        """스택에 쌓여 있는 데이터의 개수 반환"""
        return len(self.__stk)
    
    def is_empty(self) -> bool:
        return not self.__stk
    
    def is_full(self) -> bool:
        return len(self.__stk) == self.maxlen
    
    def push(self, value:Any) -> None:
        """데이터 푸시"""
        self.__stk.append(value)
    
    def pop(self) -> int:
        """데이터 팝"""
        return self.__stk.pop()
    
    def peek(self) -> int:
        """데이터 피크"""
        return self.__stk[-1]