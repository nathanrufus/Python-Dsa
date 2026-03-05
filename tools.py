import itertools

# Example: Cartesian product of two lists of integers
list1 = [1, 2]
list2 = [3, 4]

for combo in itertools.product(list1, list2):
    print(combo)
# Output:
# (1, 3)
# (1, 4)
# (2, 3)
# (2, 4)