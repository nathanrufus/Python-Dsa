"""Sliding Window Algorithm Explanation and Examples.

Sliding window is a technique for solving problems that involve arrays or strings
where you need to consider a contiguous subsequence. The idea is to maintain a
window of elements and move it across the input, updating the current state as
you go rather than recomputing from scratch.

There are two common variants:
- Fixed-size sliding window: the window length is constant.
- Dynamic-size sliding window: the window length can grow or shrink depending on
  conditions like sum, count, or unique elements.

Common use cases:
- Maximum or minimum sum/average of all subarrays of length k.
- Smallest subarray with sum at least S.
- Longest substring or subarray with certain properties, such as at most K
  distinct characters or no repeating characters.
- Finding a subarray or substring that meets a target condition, such as
  exact sum or containing all required characters.
- Problems that require a contiguous block of elements and can be updated by
  adding/removing one element at each step.
"""

from collections import defaultdict


def max_subarray_sum_fixed_window(nums, k):
    """Return maximum sum of any contiguous subarray of length k."""
    if not nums or k <= 0 or k > len(nums):
        return 0
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum


def min_subarray_length_at_least_target(nums, target):
    """Return length of smallest contiguous subarray with sum >= target."""
    left = 0
    current_sum = 0
    min_len = len(nums) + 1
    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum >= target:
            min_len = min(min_len, right - left + 1)
            current_sum -= nums[left]
            left += 1
    return min_len if min_len <= len(nums) else 0


def longest_substring_without_repeating_characters(s):
    """Return length of longest substring with no repeated characters."""
    last_seen = {}
    left = 0
    max_length = 0
    for right, ch in enumerate(s):
        if ch in last_seen and last_seen[ch] >= left:
            left = last_seen[ch] + 1
        last_seen[ch] = right
        max_length = max(max_length, right - left + 1)
    return max_length


def longest_substring_at_most_k_distinct(s, k):
    """Return length of longest substring with at most k distinct characters."""
    if k == 0:
        return 0
    count = defaultdict(int)
    left = 0
    max_length = 0
    distinct = 0
    for right, ch in enumerate(s):
        if count[ch] == 0:
            distinct += 1
        count[ch] += 1
        while distinct > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                distinct -= 1
            left += 1
        max_length = max(max_length, right - left + 1)
    return max_length


def min_window_substring(s, t):
    """Return smallest substring of s that contains all characters in t."""
    if not s or not t:
        return ""
    need = defaultdict(int)
    for ch in t:
        need[ch] += 1
    have = defaultdict(int)
    required = len(need)
    formed = 0
    left = 0
    min_len = float('inf')
    min_window = ""
    for right, ch in enumerate(s):
        have[ch] += 1
        if ch in need and have[ch] == need[ch]:
            formed += 1
        while left <= right and formed == required:
            window_len = right - left + 1
            if window_len < min_len:
                min_len = window_len
                min_window = s[left:right + 1]
            have[s[left]] -= 1
            if s[left] in need and have[s[left]] < need[s[left]]:
                formed -= 1
            left += 1
    return min_window


if __name__ == "__main__":
    # Example use cases
    print("Max sum of fixed window:", max_subarray_sum_fixed_window([2, 1, 5, 1, 3, 2], 3))
    print("Smallest subarray length >= target:", min_subarray_length_at_least_target([2, 1, 5, 2, 3, 2], 7))
    print("Longest substring without repeats:", longest_substring_without_repeating_characters("abcabcbb"))
    print("Longest substring at most k distinct:", longest_substring_at_most_k_distinct("eceba", 2))
    print("Minimum window substring:", min_window_substring("ADOBECODEBANC", "ABC"))
