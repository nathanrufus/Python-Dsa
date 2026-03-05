# Two Pointers Problem Examples

# 1. SORTED INPUT: Find two numbers that add up to a target
def two_sum_sorted(arr, target):
    """
    Find two numbers in a sorted array that add up to a target.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return (arr[left], arr[right])
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None


# 2. PAIRS OR SUBARRAYS: Check if a string is a palindrome
def is_palindrome(s):
    """
    Check if a string is a palindrome using two pointers.
    Time: O(n), Space: O(1)
    """
    left, right = 0, len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


# 2b. PAIRS OR SUBARRAYS: Longest substring without repeating characters
def longest_substring_without_repeating(s):
    """
    Find the longest substring without repeating characters.
    Time: O(n), Space: O(min(m, n)) where m is charset size
    """
    char_index = {}
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1
        
        char_index[s[right]] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length


# 3. SLIDING WINDOW: Find smallest subarray with sum >= K
def min_subarray_sum(arr, k):
    """
    Find the smallest subarray with sum >= k.
    Time: O(n), Space: O(1)
    """
    left = 0
    current_sum = 0
    min_length = float('inf')
    
    for right in range(len(arr)):
        current_sum += arr[right]
        
        while current_sum >= k and left <= right:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1
    
    return min_length if min_length != float('inf') else -1


# 3b. SLIDING WINDOW: Move all zeros to end while maintaining order
def move_zeroes(arr):
    """
    Move all zeros to the end while maintaining the relative order of non-zero elements.
    Time: O(n), Space: O(1)
    """
    left = 0
    
    for right in range(len(arr)):
        if arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
    
    return arr


# 4. LINKED LIST (SLOW-FAST POINTERS): Floyd's Cycle Detection
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    """
    Detect if a linked list has a cycle using Floyd's Cycle Detection.
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return False
    
    slow = head
    fast = head.next
    
    while slow != fast:
        if not fast or not fast.next:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True


# 4b. LINKED LIST: Find middle of linked list
def find_middle(head):
    """
    Find the middle node of a linked list using slow and fast pointers.
    Time: O(n), Space: O(1)
    """
    if not head:
        return None
    
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow


# 4c. LINKED LIST: Check if linked list is a palindrome
def is_palindrome_linked_list(head):
    """
    Check if a linked list is a palindrome.
    Time: O(n), Space: O(1)
    """
    if not head or not head.next:
        return True
    
    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Reverse second half
    prev = None
    while slow:
        next_temp = slow.next
        slow.next = prev
        prev = slow
        slow = next_temp
    
    # Compare first half and reversed second half
    left, right = head, prev
    while right:  # right will be shorter or equal in length
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    
    return True


# Test cases
if __name__ == "__main__":
    # Test 1: two_sum_sorted
    print("Test 1 - Two Sum Sorted:", two_sum_sorted([1, 2, 3, 5, 8], 10))
    
    # Test 2: is_palindrome
    print("Test 2 - Is Palindrome:", is_palindrome("racecar"))
    
    # Test 3: longest_substring_without_repeating
    print("Test 3 - Longest Substring:", longest_substring_without_repeating("abcabcbb"))
    
    # Test 4: min_subarray_sum
    print("Test 4 - Min Subarray Sum:", min_subarray_sum([2, 3, 1, 2, 4, 3], 7))
    
    # Test 5: move_zeroes
    arr = [0, 1, 0, 3, 12]
    print("Test 5 - Move Zeroes:", move_zeroes(arr))
    
    # Test 6: has_cycle
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(-4)
    head.next.next.next.next = head.next  # Create cycle
    print("Test 6 - Has Cycle:", has_cycle(head))
