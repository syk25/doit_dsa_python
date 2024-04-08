# 체인법으로 해시함수 구현하기

from __future__ import annotations
from typing import Any, Type
import hashlib

class Node:
    """해시를 구성하는 노드"""
    
    def __init__(self, key: Any, value: Any, next: Node) -> None:
        self.key = key
        self.value = value
        self.next = next

class ChainedHash:
    """체인법으로 해시클래스 구현"""
    
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity # 해시테이블의 크기
        self.table = [None] * capacity # 해시테이블 선언
    
    def hash_value(self, key: Any) -> int:
        """해시 값을 구함"""
        if isinstance(key, int):
            return key % self.capacity
        return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16)% self.capacity)
    
    def search(self, key:Any) -> Any:
        """키가 key인 원소를 검색하여 값을 반환"""
        hash = self.hash_value(key)
        p = self.table[hash]
        
        while p is not None:
            if p.key == key:
                return p.value
            p = p.next
        
        return None
    
    def add(self, key: Any, value: Any) -> bool:
        """키가 key 이고 값이 value 인 원소를 추가"""
        hash = self.hash_value(key) # 키값을 해시값으로 변환
        p = self.table[hash] # 해시값으로 노드 찾기
        
        while p is not None:
            if p.key == key:
                return False
            p = p.next
            
        temp = Node(key, value, self.table[hash])
        self.table[hash] = temp
        return True
        
    def remove(self, key: Any) -> bool:
        """키가 key인 원소 삭제"""
        hash = self.hash_value(key) # 키를 해시값으로 변환
        p = self.table[hash] # 노드 확인
        pp = None
        
        while p is not None: 
            if p.key == key:
                if pp is None:
                    self.table[hash] = p.next
                else:
                    pp.next = p.next
                return  True
            pp = p
            p = p.next
        return False
    
    def dump(self) -> None:
        """해시 테이블을 덤프"""
        for i in range(self.capacity):
            p = self.table[i]
            print(i, end =' ')
            while p is not None:
                print(f' -> {p.key} ({p.value})', end=' ')
                p = p.next
            print()
