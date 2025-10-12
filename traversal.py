from collections import deque
import os
from typing import Any, Dict, List, Optional, Set

"""
traversal.py

Examples of common traversal techniques in Python:
- Binary tree: recursive & iterative preorder, inorder, postorder, level-order (BFS)
- Graph (adjacency list): DFS recursive, DFS iterative, BFS
- Linked list: simple traversal
- Filesystem: os.walk and manual stack-based traversal

Run as a script to see small demonstrations.
"""



# -------------------------
# Binary tree traversals
# -------------------------
class TreeNode:
    def __init__(self, val: Any, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val})"


def preorder_recursive(node: Optional[TreeNode], out: List[Any]) -> None:
    if not node:
        return
    out.append(node.val)
    preorder_recursive(node.left, out)
    preorder_recursive(node.right, out)


def inorder_recursive(node: Optional[TreeNode], out: List[Any]) -> None:
    if not node:
        return
    inorder_recursive(node.left, out)
    out.append(node.val)
    inorder_recursive(node.right, out)


def postorder_recursive(node: Optional[TreeNode], out: List[Any]) -> None:
    if not node:
        return
    postorder_recursive(node.left, out)
    postorder_recursive(node.right, out)
    out.append(node.val)


def preorder_iterative(root: Optional[TreeNode]) -> List[Any]:
    if not root:
        return []
    stack = [root]
    out: List[Any] = []
    while stack:
        node = stack.pop()
        out.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return out


def inorder_iterative(root: Optional[TreeNode]) -> List[Any]:
    out: List[Any] = []
    stack: List[TreeNode] = []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        out.append(curr.val)
        curr = curr.right
    return out


def postorder_iterative(root: Optional[TreeNode]) -> List[Any]:
    # Two-stack method
    if not root:
        return []
    stack1 = [root]
    stack2: List[TreeNode] = []
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    return [n.val for n in reversed(stack2)]


def level_order_bfs(root: Optional[TreeNode]) -> List[List[Any]]:
    levels: List[List[Any]] = []
    if not root:
        return levels
    q = deque([root])
    while q:
        level_size = len(q)
        level: List[Any] = []
        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        levels.append(level)
    return levels


# -------------------------
# Graph traversals
# -------------------------
def dfs_recursive(graph: Dict[Any, List[Any]], src: Any, visited: Optional[Set[Any]] = None, out: Optional[List[Any]] = None):
    if visited is None:
        visited = set()
    if out is None:
        out = []
    visited.add(src)
    out.append(src)
    for nei in graph.get(src, []):
        if nei not in visited:
            dfs_recursive(graph, nei, visited, out)
    return out


def dfs_iterative(graph: Dict[Any, List[Any]], src: Any) -> List[Any]:
    visited: Set[Any] = set()
    stack = [src]
    out: List[Any] = []
    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        out.append(node)
        # push neighbors in reverse to mimic recursive order
        for nei in reversed(graph.get(node, [])):
            if nei not in visited:
                stack.append(nei)
    return out


def bfs_graph(graph: Dict[Any, List[Any]], src: Any) -> List[Any]:
    visited: Set[Any] = {src}
    q = deque([src])
    out: List[Any] = []
    while q:
        node = q.popleft()
        out.append(node)
        for nei in graph.get(node, []):
            if nei not in visited:
                visited.add(nei)
                q.append(nei)
    return out


# -------------------------
# Linked list traversal
# -------------------------
class ListNode:
    def __init__(self, val: Any, nxt: Optional["ListNode"] = None):
        self.val = val
        self.next = nxt

    def __repr__(self):
        return f"ListNode({self.val})"


def traverse_linked_list(head: Optional[ListNode]) -> List[Any]:
    out: List[Any] = []
    curr = head
    while curr:
        out.append(curr.val)
        curr = curr.next
    return out


# -------------------------
# Filesystem traversal
# -------------------------
def traverse_os_walk(start_path: str, max_items: int = 20) -> List[str]:
    """Return first few paths discovered by os.walk (top-down)."""
    found: List[str] = []
    for root, dirs, files in os.walk(start_path):
        found.append(root)
        found.extend(os.path.join(root, f) for f in files)
        if len(found) >= max_items:
            break
    return found[:max_items]


def traverse_manual_stack(start_path: str, max_items: int = 20) -> List[str]:
    """Manual DFS using a stack with os.listdir."""
    found: List[str] = []
    stack = [start_path]
    while stack and len(found) < max_items:
        path = stack.pop()
        found.append(path)
        if os.path.isdir(path):
            try:
                entries = [os.path.join(path, e) for e in os.listdir(path)]
            except PermissionError:
                continue
            # push in reversed order to visit lexicographically
            for e in sorted(entries, reverse=True):
                stack.append(e)
    return found


# -------------------------
# Demo / simple tests
# -------------------------
def _build_sample_tree():
    # builds:
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n2 = TreeNode(2, n4, n5)
    n3 = TreeNode(3, None, n6)
    return TreeNode(1, n2, n3)


def _build_sample_graph():
    # directed graph (adj list)
    return {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": []
    }


def _build_linked_list():
    # 1 -> 2 -> 3
    return ListNode(1, ListNode(2, ListNode(3)))


if __name__ == "__main__":
    # Binary tree demos
    tree = _build_sample_tree()
    print("Preorder recursive:", (lambda o=[]: (preorder_recursive(tree, o), o)[1])([]))
    print("Inorder recursive:", (lambda o=[]: (inorder_recursive(tree, o), o)[1])([]))
    print("Postorder recursive:", (lambda o=[]: (postorder_recursive(tree, o), o)[1])([]))
    print("Preorder iterative:", preorder_iterative(tree))
    print("Inorder iterative:", inorder_iterative(tree))
    print("Postorder iterative:", postorder_iterative(tree))
    print("Level-order (BFS):", level_order_bfs(tree))

    # Graph demos
    g = _build_sample_graph()
    print("DFS recursive:", dfs_recursive(g, "A"))
    print("DFS iterative:", dfs_iterative(g, "A"))
    print("BFS graph:", bfs_graph(g, "A"))

    # Linked list demo
    ll = _build_linked_list()
    print("Linked list traverse:", traverse_linked_list(ll))

    # Filesystem demo (current directory; safe small output)
    cwd = os.getcwd()
    print("os.walk sample (cwd):", traverse_os_walk(cwd, max_items=6))
    print("manual stack DFS (cwd):", traverse_manual_stack(cwd, max_items=6))