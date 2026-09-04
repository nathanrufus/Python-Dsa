"""In-place linked-list reversal algorithms."""


class ListNode:
	def __init__(self, value=0, next_node=None):
		self.val = value
		self.next = next_node


def reverse_list(head):
	"""Reverse the entire linked list in O(n) time and O(1) space."""
	prev = None
	curr = head
	while curr:
		nxt = curr.next
		curr.next = prev
		prev = curr
		curr = nxt
	return prev


def reverse_between(head, m, n):
	"""Reverse the one-indexed sublist from position m through n."""
	if not head or m == n:
		return head

	dummy = ListNode(next_node=head)
	before = dummy
	for _ in range(m - 1):
		before = before.next

	curr = before.next
	for _ in range(n - m):
		nxt = curr.next
		curr.next = nxt.next
		nxt.next = before.next
		before.next = nxt
	return dummy.next


def reverse_k_group(head, k):
	"""Reverse complete groups of k nodes, leaving a short final group intact."""
	if k <= 1 or not head:
		return head

	dummy = ListNode(next_node=head)
	group_prev = dummy
	while True:
		group_end = group_prev
		for _ in range(k):
			group_end = group_end.next
			if not group_end:
				return dummy.next

		group_next = group_end.next
		prev, curr = group_next, group_prev.next
		while curr is not group_next:
			nxt = curr.next
			curr.next = prev
			prev = curr
			curr = nxt

		old_start = group_prev.next
		group_prev.next = group_end
		group_prev = old_start
