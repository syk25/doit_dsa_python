from typing import Any
import sys

N = int(sys.stdin.readline().strip())

tree = {}

for i in range(N):
    node = [x for x in sys.stdin.readline().split()]
    tree[node[0]] = [node[1], node[2]]


def preorder(root: str = "A", tree: dict = tree) -> None:
    parent = tree[root]
    print(root, end="")
    left = parent[0]
    right = parent[1]
    if left != ".":
        preorder(left)
    if right != ".":
        preorder(right)


def inorder(root: str = "A", tree: dict = tree) -> None:
    parent = tree[root]
    left = parent[0]
    right = parent[1]
    if left != ".":
        inorder(left)
    print(root, end="")
    if right != ".":
        inorder(right)


def postorder(root: str = "A", tree: dict = tree) -> None:
    parent = tree[root]
    left = parent[0]
    right = parent[1]
    if left != ".":
        postorder(left)
    if right != ".":
        postorder(right)
    print(root, end="")


preorder()
print()
inorder()
print()
postorder()
print()
