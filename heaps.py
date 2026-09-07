"""Top K Elements — heap notes.

Use heapq's min-heap directly for K largest values.  For K smallest values,
store negatives to simulate a max-heap.  Keeping the heap bounded by K gives
O(n log k) time and O(k) space.

"""

import heapq
from collections import Counter


def kth_largest(nums, k):
	"""LC 215: return the kth largest element."""
	heap = []
	for value in nums:
		heapq.heappush(heap, value)
		if len(heap) > k:
			heapq.heappop(heap)
	return heap[0]


def top_k_frequent(nums, k):
	"""LC 347: return the k most frequent values."""
	counts = Counter(nums)
	heap = []
	for value, frequency in counts.items():
		heapq.heappush(heap, (frequency, value))
		if len(heap) > k:
			heapq.heappop(heap)
	return [value for _, value in heap]


def k_closest_points(points, k):
	"""LC 973: return the k points closest to the origin."""
	heap = []  # max-heap via negative distance
	for x, y in points:
		distance = x * x + y * y
		heapq.heappush(heap, (-distance, x, y))
		if len(heap) > k:
			heapq.heappop(heap)
	return [[x, y] for _, x, y in heap]


def frequency_sort(s):
	"""LC 451: sort characters by decreasing frequency."""
	return "".join(
		character * frequency
		for frequency, character in sorted(
			((frequency, character) for character, frequency in Counter(s).items()),
			reverse=True,
		)
	)


class MedianFinder:
	"""LC 295: two heaps keep the lower and upper halves balanced."""

	def __init__(self):
		self.lower = []  # max-heap represented by negative values
		self.upper = []  # min-heap

	def add_num(self, number):
		heapq.heappush(self.lower, -number)
		heapq.heappush(self.upper, -heapq.heappop(self.lower))
		if len(self.upper) > len(self.lower):
			heapq.heappush(self.lower, -heapq.heappop(self.upper))

	def find_median(self):
		if len(self.lower) > len(self.upper):
			return float(-self.lower[0])
		return (-self.lower[0] + self.upper[0]) / 2


def reorganize_string(s):
	"""LC 767: rearrange so adjacent characters differ, or return ''."""
	counts = Counter(s)
	if max(counts.values(), default=0) > (len(s) + 1) // 2:
		return ""

	heap = [(-frequency, character) for character, frequency in counts.items()]
	heapq.heapify(heap)
	result = []
	previous = (0, "")
	while heap:
		frequency, character = heapq.heappop(heap)
		result.append(character)
		if previous[0] < 0:
			heapq.heappush(heap, previous)
		frequency += 1
		previous = (frequency, character)
	return "".join(result)
