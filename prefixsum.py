arr=[4 ,7, 1, 3, 2]
prefix_sum = [0] * len(arr)
prefix_sum[0] = arr[0]
for i in range(1, len(arr)):
    prefix_sum[i] = prefix_sum[i-1] + arr[i]
print(prefix_sum)


# Challenge 1: Range Sum Query
def rangeSum(prefix_sum, left, right):
    if left == 0:
        return prefix_sum[right]
    return prefix_sum[right] - prefix_sum[left - 1]

print("Range sum [1,3]:", rangeSum(prefix_sum, 1, 3))

# Challenge 2: Find equilibrium point (sum of left = sum of right)
def equilibriumPoint(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    
    total = prefix[-1]
    left_sum = 0
    for i in range(len(arr)):
        right_sum = total - left_sum - arr[i]
        if left_sum == right_sum:
            return i
        left_sum += arr[i]
    return -1

# Challenge 3: Count subarrays with sum equals K
def subarraySum(arr, k):
    count = 0
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i, len(arr)):
            current_sum += arr[j]
            if current_sum == k:
                count += 1
    return count

# Challenge 4: Maximum subarray sum (Kadane's with prefix)
def maxSubarraySum(arr):
    max_sum = arr[0]
    current_sum = 0
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Challenge 5: Product of array except self
def productExceptSelf(arr):
    n = len(arr)
    result = [1] * n
    prefix_prod = 1
    for i in range(n):
        result[i] = prefix_prod
        prefix_prod *= arr[i]
    suffix_prod = 1
    for i in range(n-1, -1, -1):
        result[i] *= suffix_prod
        suffix_prod *= arr[i]
    return result

print("Product except self:", productExceptSelf(arr))