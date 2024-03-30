from __future__ import annotations
from typing import Any, Type


class Node:
    """이진검색트리의 노드"""

    def __init__(self, key: Any, value: Any, left: Node = None, right: Node = None):
        """생성자"""
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree:
    """이진검색트리"""

    def __init__(self):
        """초기화"""
        self.root = None

    def search(self, key: Any) -> Any:
        """검색"""
        p = self.root

        while p is not None:
            if p is None:
                return None
            if key == p.key:
                return p.value
            elif key < p.key:
                p = self.left
            else:
                p = self.right

    def add(self, key: Any, value:Any) -> Any:
        """노드 삽입"""
        
        def add_node(node:Node, key:Any, value: Any) -> None:
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value, None, None)
                else:
                    add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value, None, None)
                else:
                    add_node(node.right, key, value)
            return True
        
        if self.root is None:
            self.root = Node(key, value, None, None)
            return True
        else:
            return add_node(self.root, key, value)
        