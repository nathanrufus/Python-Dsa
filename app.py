from collections import defaultdict
from collections import Counter
import sys

# Dictionary Operations and Examples in Python

# 1. Creating a dictionary
d = {'a': 1, 'b': 2, 'c': 3}
d2 = dict(x=10, y=20)
d3 = dict([('k1', 100), ('k2', 200)])

# 2. Accessing values
print(d['a'])         # 1
print(d.get('b'))     # 2
print(d.get('z', 0))  # 0 (default if key not found)

# 3. Adding/Updating items
d['d'] = 4            # Add new key
d['a'] = 10           # Update value

# 4. Removing items
del d['b']            # Remove key 'b'
removed = d.pop('c')  # Remove and return value for 'c'
d.popitem()           # Remove and return last inserted item (Python 3.7+)
d.clear()             # Remove all items

# 5. Checking existence
print('a' in d)       # True/False
print('z' not in d)   # True/False

# 6. Iterating
for key in d2:
    print(key, d2[key])

for key, value in d2.items():
    print(key, value)

for value in d2.values():
    print(value)

for key in d2.keys():
    print(key)

# 7. Dictionary methods
d4 = {'x': 1, 'y': 2}
d5 = {'y': 3, 'z': 4}
d4.update(d5)         # Merge d5 into d4

copy_d4 = d4.copy()   # Shallow copy

# fromkeys
keys = ['a', 'b', 'c']
default_dict = dict.fromkeys(keys, 0)  # {'a': 0, 'b': 0, 'c': 0}

# setdefault
d4.setdefault('w', 100)  # Adds 'w' with value 100 if not present

# 8. Dictionary comprehension
squares = {x: x*x for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}

# 9. Length
print(len(d4))         # Number of items

# 10. Nested dictionaries
nested = {'outer': {'inner': 42}}
print(nested['outer']['inner'])

# 11. Sorting keys/values
for k in sorted(d4):
    print(k, d4[k])

# 12. Unpacking dictionary
def func(a, b, c):
    print(a, b, c)
params = {'a': 1, 'b': 2, 'c': 3}
func(**params)

# 13. Dictionary views
keys_view = d4.keys()
values_view = d4.values()
items_view = d4.items()

# 14. Merging dictionaries (Python 3.9+)
d6 = {**d4, **d5}
d7 = d4 | d5

# 15. Reversing key-value pairs
reversed_dict = {v: k for k, v in d4.items()}

# 16. Defaultdict (from collections)
dd = defaultdict(int)
dd['missing'] += 1

# 17. Counter (from collections)
cnt = Counter(['a', 'b', 'a', 'c', 'b', 'a'])

# 18. Dictionary as function argument
def show(**kwargs):
    print(kwargs)
show(a=1, b=2)

# 19. Dictionary equality
d8 = {'x': 1, 'y': 2}
d9 = {'y': 2, 'x': 1}  
print(d8 == d9)  # True

# 20. Dictionary memory usage
print(sys.getsizeof(d8))

# 21. Dictionary with tuple keys
tuple_key_dict = {(1, 2): 'point'}

# 22. Dictionary with mutable values
d10 = {'list': [1, 2, 3]}
d10['list'].append(4)

# 23. Removing all items (clear)
d10.clear()

# 24. Creating dictionary from two lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict_from_lists = dict(zip(keys, values))

# 25. Dictionary string representation
print(str(d4))
print(repr(d4))