# 이진탐색트리


class Node:
    """노드"""
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BSTree:
    """이진탐색트리"""
    def __init__(self):
        self.root = None

