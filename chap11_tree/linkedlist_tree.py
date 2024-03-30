# 연결리스트로 이진트리 표현
# 1. 노드 정의하기
# 2. 트리 정의하기

from typing import Any
from collections import deque


class Node:
    """노드: 키, left, right 값을 가짐"""

    def __init__(self, key: Any):
        self.key = key
        self.left = None
        self.right = None


class Tree:
    """트리 구현: root"""

    def __init__(self):
        self.root = None

    def level_traversal(self):
        if not self.root:
            return []

        reservation = deque()
        visited = []

        reservation.append(self.root)

        while reservation:
            current_node = reservation.popleft()
            visited.append(current_node)

            if current_node.left is not None:
                reservation.append(current_node.left)
            if current_node.right is not None:
                reservation.append(current_node.right)

        return visited

    def in_order_traversal(self):
        def in_order(node):
            if node is None:
                return
            in_order(node.left)
            res.append(node.key)
            in_order(node.right)
        
        res = []
        in_order(self.root)
        return res
    
    def post_order_traversal(self):
        def post_order(node):
            if node is None:
                return
            post_order(node.left)
            post_order(node.right)
            res.append(node.key)
        
        res = []
        post_order(self.root)
        return res


if __name__ == "__main__":
    tree = Tree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")
    tree.root.right.right = Node("G")

    print(tree)
    print(*[x.key for x in tree.level_traversal()])
    print(tree.in_order_traversal())
    print(tree.post_order_traversal())
