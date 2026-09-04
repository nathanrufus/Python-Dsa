"""
07. Modified Binary Search
Intermediate · 3 days

Binary search on rotated arrays, answer spaces, or partially sorted data.
Key insight: one half is always sorted — determine which half to search.

TIME COMPLEXITY: O(log n)
SPACE COMPLEXITY: O(1)

TEMPLATE:
    l, r = 0, n - 1
    while l <= r:
        mid = (l + r) // 2
        if found:
            return mid
        elif go_left:
            r = mid - 1
        else:
            l = mid + 1

MOST COMMONLY ASKED QUESTIONS:
1. Binary Search (#704, Easy) - Classic binary search
2. Search in Rotated Sorted Array (#33, Medium) - Find target in rotated sorted array
3. Find Minimum in Rotated Sorted Array (#153, Medium) - Find minimum element
4. Search a 2D Matrix (#74, Medium) - Binary search in 2D matrix
5. Koko Eating Bananas (#875, Medium) - Binary search on answer space
6. Find Minimum in Rotated Sorted Array II (#154, Hard) - With duplicates

KEY INSIGHTS:
- One half of the array is always sorted in rotated arrays
- Use the sorted half to determine search direction
- Handle edge cases: duplicates, single element, all same elements
- Binary search on answer space: find minimum value that satisfies condition
- For 2D matrices, treat as 1D sorted array and use index conversion
"""

# Example: Search in Rotated Sorted Array
def search_rotated(nums, target):
    """Find target in rotated sorted array. Returns index or -1."""
    l, r = 0, len(nums) - 1
    
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        
        # Left half is sorted
        if nums[l] <= nums[mid]:
            if nums[l] <= target < nums[mid]:
                r = mid - 1  # Target in left half
            else:
                l = mid + 1  # Target in right half
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[r]:
                l = mid + 1  # Target in right half
            else:
                r = mid - 1  # Target in left half
    
    return -1


# Example: Find Minimum in Rotated Sorted Array
def find_min_rotated(nums):
    """Find minimum element in rotated sorted array."""
    l, r = 0, len(nums) - 1
    
    while l < r:
        mid = (l + r) // 2
        
        # Right half is sorted, min is on left
        if nums[mid] > nums[r]:
            l = mid + 1
        # Left half is sorted (or mid is minimum), min is on left
        else:
            r = mid
    
    return nums[l]


# Example: Binary Search on Answer Space (Koko Eating Bananas)
def min_eating_speed(piles, h):
    """Find minimum eating speed to finish all piles in h hours."""
    l, r = 1, max(piles)
    
    def can_finish(speed):
        hours = sum((pile + speed - 1) // speed for pile in piles)  # Ceiling division
        return hours <= h
    
    while l < r:
        mid = (l + r) // 2
        if can_finish(mid):
            r = mid  # Try slower speed
        else:
            l = mid + 1  # Need faster speed
    
    return l




