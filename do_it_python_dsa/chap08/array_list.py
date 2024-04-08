# 커서로 연결리스트 구현

from __future__ import annotations
from typing import Any, Type

Null = -1

class Node:
    """연결리스트용 노드 클래스"""
    
    def __init__(self, data = Null, next = Null, dnext = Null):
        """초기화"""
        self.data = data
        self.next = next
        self.dnext = dnext

class ArrayList:
    """연결리스트(배열 커서 버전)"""
    def __init__(self, capacity:int):
        """초기화"""
        self.head = Null
        self.current = Null
        self.max = Null
        self.deleted = Null
        self.capacity = capacity
        self.n = [Node()] * self.capacity
        self.no = 0

    def __len__(self) -> int:
        """연결리스트의 노드 수를 반환"""
        return self.no
    
    def get_insert_index(self):
        """다음에 삽입할 레코드의 인덱스를 구함"""
        if self.deleted == Null:
            if self.max + 1 < self.capacity:
                self.max += 1
                return self.max
            else:
                return Null
        else:
            rec = self.deleted
            self.deleted = self.n[rec].dnext
            return rec
    
    def delete_index(self, idx: int) -> None:
        """레코드 idx를 프리 리스트에 등록"""
        if self.deleted == Null:
            self.deleted = idx
            self.n[idx].dnext = Null
        else:
            rec = self.deleted
            self.deleted = idx
            self.n[idx].dnext = rec
            