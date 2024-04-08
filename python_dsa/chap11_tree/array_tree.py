from typing import Any

my_tree = ["A", "B", "C", "D", "E", "F", None, "G"]


def print_tree(tree: list) -> None:
    i = 0
    n = len(my_tree)

    while i < n:
        if my_tree[i]:
            print(f"Parent: {my_tree[i]}", end=", ")
            left = 2 * i + 1
            right = 2 * i + 2
        if left < n and my_tree[left] is not None:
            print(f"Left: {my_tree[left]}", end=", ")
        if right < n and my_tree[right] is not None:
            print(f"Right: {my_tree[right]}", end=", ")
        print()
    i += 1


def find_parent(child: Any, tree: list) -> None:
    child_idx = tree.index(child)
    parent_idx = 0
    if child_idx % 2 == 1:
        parent_idx = (child_idx - 1) // 2
    else:
        parent_idx = (child_idx - 2) // 2
    print(f"Parent of {child}: {tree[parent_idx]}")


def pre_order(tree: Any, i=0) -> None:
    """트리의 전위순회"""
    if i < len(tree):
        print(tree[i], end=" ")
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(tree) and tree[left] is not None:
            pre_order(tree, left)
        if right < len(tree) and tree[right] is not None:
            pre_order(tree, right)


def in_order(tree: Any, i=0) -> None:
    """트리의 중위순회"""
    if i < len(tree):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(tree) and tree[left] is not None:
            in_order(tree, left)
        print(tree[i], end=" ")
        if right < len(tree) and tree[right] is not None:
            in_order(tree, right)


def post_order(tree: Any, i=0) -> None:
    """트리의 후위순회"""
    if i < len(tree):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(tree) and tree[left] is not None:
            post_order(tree, left)
        if right < len(tree) and tree[right] is not None:
            post_order(tree, right)
        print(tree[i], end=" ")


def pre_order_stk(tree: list, i=0) -> Any:
    if not tree:
        return []
    res, stack = [], [0]
    while stack:
        parent = stack.pop()
        res.append(tree[parent])
        left = 2 * parent + 1
        right = 2 * parent + 2
        if right < len(tree) and tree[right] is not None:
            stack.append(right)
        if left < len(tree) and tree[left] is not None:
            stack.append(left)
    return res


print("pre-order", pre_order_stk(my_tree))
