import sys
sys.setrecursionlimit(10**7)

nodes = [int(line.strip()) for line in sys.stdin.readlines()]


class Node:
    """노드 정의"""

    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BSTree:
    """이진검색트리"""

    def __init__(self):
        """트리의 초기화"""
        self.root = None

    def add(self, data: int):
        """데이터 추가하기"""
        if self.root is None:
            self.root = Node(data)
            return

        current = self.root
        while True:
            if current.value < data:
                if current.right is None:
                    current.right = Node(data)
                    break
                current = current.right
            elif current.value > data:
                if current.left is None:
                    current.left = Node(data)
                    break
                current = current.left


    def postorder(self):
        """트리의 후위순회"""
        def post_order(node):

            if node is None:
                return
            post_order(node.left)
            post_order(node.right)
            print(node.value)
        
        post_order(self.root)

tree = BSTree()
for i in nodes:
    tree.add(i)

tree.postorder()
