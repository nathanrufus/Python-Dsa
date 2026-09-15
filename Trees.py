"""Trees in data structures: examples from easy to hard.

Run this file to see the output.  A tree is a hierarchical, non-linear
structure made of nodes connected by edges.  The top node is the root.
"""


# 1) EASY: A simple binary tree
# Each node has at most two children: left and right.
class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


def simple_tree():
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	return root


# Short note: A leaf is a node with no children.  Here, 3 and 4 are leaves.


# 2) EASY: Tree traversal
# Preorder: root -> left -> right.  Useful for copying/serializing a tree.
def preorder(root):
	if root is None:
		return []
	return [root.value] + preorder(root.left) + preorder(root.right)


# Inorder: left -> root -> right.  For a binary search tree, it is sorted.
def inorder(root):
	if root is None:
		return []
	return inorder(root.left) + [root.value] + inorder(root.right)


# Postorder: left -> right -> root.  Useful when deleting a tree.
def postorder(root):
	if root is None:
		return []
	return postorder(root.left) + postorder(root.right) + [root.value]


# 3) MEDIUM: Level-order traversal (breadth-first search)
# A queue visits nodes one level at a time.
def level_order(root):
	if root is None:
		return []

	queue = [root]
	result = []
	while queue:
		node = queue.pop(0)  # deque would be faster for very large trees.
		result.append(node.value)
		if node.left:
			queue.append(node.left)
		if node.right:
			queue.append(node.right)
	return result


# 4) MEDIUM: Binary Search Tree (BST)
# Rule: values smaller than a node go left; larger values go right.
def bst_insert(root, value):
	if root is None:
		return Node(value)
	if value < root.value:
		root.left = bst_insert(root.left, value)
	elif value > root.value:
		root.right = bst_insert(root.right, value)
	return root  # Duplicate values are ignored.


def bst_search(root, target):
	if root is None or root.value == target:
		return root
	if target < root.value:
		return bst_search(root.left, target)
	return bst_search(root.right, target)


# 5) HARD: Delete a value from a BST
# Three cases: leaf, one child, or two children.  For two children, replace
# with the smallest value in the right subtree (the inorder successor).
def bst_delete(root, value):
	if root is None:
		return None
	if value < root.value:
		root.left = bst_delete(root.left, value)
	elif value > root.value:
		root.right = bst_delete(root.right, value)
	else:
		if root.left is None:
			return root.right
		if root.right is None:
			return root.left
		successor = root.right
		while successor.left:
			successor = successor.left
		root.value = successor.value
		root.right = bst_delete(root.right, successor.value)
	return root


# 6) HARD: Height and balance
# Height is the longest path from a node to a leaf.  A balanced tree keeps
# left/right subtree heights close, helping operations stay near O(log n).
def height(root):
	if root is None:
		return 0
	return 1 + max(height(root.left), height(root.right))


def is_balanced(root):
	def check(node):
		if node is None:
			return 0
		left_height = check(node.left)
		if left_height == -1:
			return -1
		right_height = check(node.right)
		if right_height == -1 or abs(left_height - right_height) > 1:
			return -1
		return 1 + max(left_height, right_height)

	return check(root) != -1


# 7) HARD: Lowest Common Ancestor in a BST
# The first node where targets split into different branches is the answer.
def lowest_common_ancestor(root, first, second):
	while root:
		if first < root.value and second < root.value:
			root = root.left
		elif first > root.value and second > root.value:
			root = root.right
		else:
			return root
	return None


if __name__ == "__main__":
	tree = simple_tree()
	print("Preorder:", preorder(tree))
	print("Inorder:", inorder(tree))
	print("Postorder:", postorder(tree))
	print("Level order:", level_order(tree))

	bst = None
	for number in [8, 3, 10, 1, 6, 14, 4, 7, 13]:
		bst = bst_insert(bst, number)
	print("BST inorder:", inorder(bst))
	print("Search 7:", bst_search(bst, 7) is not None)
	print("Height:", height(bst), "Balanced:", is_balanced(bst))
	print("LCA of 4 and 7:", lowest_common_ancestor(bst, 4, 7).value)
	bst = bst_delete(bst, 3)
	print("After deleting 3:", inorder(bst))


"""Complexity notes (n = number of nodes):
- Traversals, height, and balance check: O(n) time; recursion uses O(h) space.
- BST search/insert/delete: O(h) time, where h is tree height.
- Balanced BST: O(log n) average/worst-case operations.
- Unbalanced BST: O(n) worst-case operations.
"""
