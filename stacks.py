"""Monotonic Stack notes and common LeetCode solutions.

A monotonic stack stores indices (or values) in increasing/decreasing order.
When a new value breaks the invariant, pop until the invariant is restored.
Each item is pushed and popped at most once: O(n) time and O(n) space.

Template (next greater element):
	stack = []
	for i, x in enumerate(arr):
		while stack and arr[stack[-1]] < x:
			process(stack.pop(), i)
		stack.append(i)

Use a decreasing stack for next-greater queries and an increasing stack for
next-smaller queries. Store indices when distances or ranges are required.
"""


def daily_temperatures(temperatures):
	"""LeetCode 739: days until a warmer temperature."""
	answer = [0] * len(temperatures)
	stack = []  # indices, temperatures decrease from bottom to top
	for i, temperature in enumerate(temperatures):
		while stack and temperatures[stack[-1]] < temperature:
			previous = stack.pop()
			answer[previous] = i - previous
		stack.append(i)
	return answer


def next_greater_element(nums1, nums2):
	"""LeetCode 496: next greater value for each value in nums1."""
	next_value = {}
	stack = []
	for value in nums2:
		while stack and stack[-1] < value:
			next_value[stack.pop()] = value
		stack.append(value)
	return [next_value.get(value, -1) for value in nums1]


def next_greater_elements(nums):
	"""LeetCode 503: next greater values in a circular array."""
	answer = [-1] * len(nums)
	stack = []
	for i in range(2 * len(nums)):
		index = i % len(nums)
		while stack and nums[stack[-1]] < nums[index]:
			answer[stack.pop()] = nums[index]
		if i < len(nums):
			stack.append(index)
	return answer


def largest_rectangle_area(heights):
	"""LeetCode 84: largest rectangle in a histogram."""
	stack = []  # (start index, height), increasing heights
	best = 0
	for i, height in enumerate(heights + [0]):
		start = i
		while stack and stack[-1][1] > height:
			previous_start, previous_height = stack.pop()
			best = max(best, previous_height * (i - previous_start))
			start = previous_start
		stack.append((start, height))
	return best


def remove_k_digits(num, k):
	"""LeetCode 402: remove k digits to form the smallest number."""
	stack = []
	for digit in num:
		while k and stack and stack[-1] > digit:
			stack.pop()
			k -= 1
		stack.append(digit)
	if k:
		stack = stack[:-k]
	return "".join(stack).lstrip("0") or "0"


def sum_subarray_mins(arr):
	"""LeetCode 907: sum of minimums of all subarrays."""
	mod = 10**9 + 7
	total = 0
	stack = []  # (value, count); values are increasing
	for value in arr:
		count = 1
		while stack and stack[-1][0] >= value:
			old_value, old_count = stack.pop()
			count += old_count
			total -= old_value * old_count
		stack.append((value, count))
		total += value * count
		total %= mod
	# Each stack entry contributes to subarrays ending at the final position.
	return sum(value * count for value, count in stack) % mod


class Mystack:
    def __init__(self,capacity):
        self.capacity=capacity
        self.stack=[0]*capacity
        self.top=-1

    def push(self,value):
        if self.top==self.capacity-1:
            print("Stack is full")
            return
        self.top+=1
        self.stack[self.top]=value