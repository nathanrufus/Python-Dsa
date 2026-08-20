"""Week 03: Linked Lists & Searching — fast and slow pointers.

The slow pointer advances one node at a time and the fast pointer advances
two.  This gives O(n) time and O(1) extra space for the linked-list problems
below (apart from the optional list-building helpers).
"""


class ListNode:
	"""A singly linked-list node."""

	def __init__(self, val=0, next_node=None):
		self.val = val
		self.next = next_node


def has_cycle(head):
	"""LeetCode 141, Easy: return whether a linked list contains a cycle.

	If the pointers meet, fast has looped around and a cycle must exist.
	"""
	slow = fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow is fast:
			return True
	return False


def cycle_start(head):
	"""LeetCode 142, Medium: return the first node in a cycle, or None.

	After a meeting, resetting one pointer to head makes the next meeting the
	cycle entrance.  Time O(n), extra space O(1).
	"""
	slow = fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
		if slow is fast:
			from_head = head
			while from_head is not slow:
				from_head = from_head.next
				slow = slow.next
			return from_head
	return None


def find_duplicate(nums):
	"""LeetCode 287, Medium: find the duplicate in 1..n without extra space.

	Treat each value as the next array index.  A duplicate creates a cycle;
	Floyd's algorithm finds its entrance.  Time O(n), extra space O(1).
	"""
	slow = fast = nums[0]
	while True:
		slow = nums[slow]
		fast = nums[nums[fast]]
		if slow == fast:
			break

	slow = nums[0]
	while slow != fast:
		slow = nums[slow]
		fast = nums[fast]
	return slow


def middle_node(head):
	"""LeetCode 876, Easy: return the middle node.

	For an even-length list, this returns the second middle node.
	"""
	slow = fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next
	return slow


def is_happy(n):
	"""LeetCode 202, Easy: determine whether repeated digit squares reach 1.

	Repetition means the sequence is stuck in a cycle that does not contain 1.
	"""
	def next_number(value):
		total = 0
		while value:
			value, digit = divmod(value, 10)
			total += digit * digit
		return total

	slow = next_number(n)
	fast = next_number(next_number(n))
	while slow != fast:
		slow = next_number(slow)
		fast = next_number(next_number(fast))
	return slow == 1


def is_palindrome(head):
	"""LeetCode 234, Easy: check a list using O(1) extra space.

	Find the midpoint, reverse the second half, then compare both halves.
	"""
	if not head or not head.next:
		return True

	slow = fast = head
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

	previous = None
	while slow:
		following = slow.next
		slow.next = previous
		previous = slow
		slow = following

	left, right = head, previous
	while right:
		if left.val != right.val:
			return False
		left = left.next
		right = right.next
	return True
