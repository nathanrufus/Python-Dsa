"""
Hash Table Examples: Simple to Complex
"""

# ============================================================================
# 1. SIMPLE HASH TABLE - Manual Implementation with Linear Probing
# ============================================================================

class SimpleHashTable:
    """Basic hash table with linear probing for collision handling"""
    
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        """Simple hash function"""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert key-value pair"""
        index = self.hash_function(key)
        
        # Linear probing for collision handling
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (index + 1) % self.size
        
        self.table[index] = (key, value)
    
    def search(self, key):
        """Search for a key"""
        index = self.hash_function(key)
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
        
        return None
    
    def delete(self, key):
        """Delete a key"""
        index = self.hash_function(key)
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                return True
            index = (index + 1) % self.size
        
        return False


# ============================================================================
# 2. HASH TABLE WITH CHAINING - Using Linked Lists
# ============================================================================

class Node:
    """Node for linked list in chaining"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class ChainingHashTable:
    """Hash table using separate chaining with linked lists"""
    
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
    
    def hash_function(self, key):
        """Hash function"""
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert using chaining"""
        index = self.hash_function(key)
        
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            # Check if key exists and update, or add to chain
            current = self.table[index]
            while current:
                if current.key == key:
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            current.next = Node(key, value)
    
    def search(self, key):
        """Search in chain"""
        index = self.hash_function(key)
        current = self.table[index]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        return None
    
    def delete(self, key):
        """Delete from chain"""
        index = self.hash_function(key)
        
        if self.table[index] is None:
            return False
        
        if self.table[index].key == key:
            self.table[index] = self.table[index].next
            return True
        
        current = self.table[index]
        while current.next:
            if current.next.key == key:
                current.next = current.next.next
                return True
            current = current.next
        
        return False


# ============================================================================
# 3. DYNAMIC HASH TABLE - With Resizing
# ============================================================================

class DynamicHashTable:
    """Hash table that resizes when load factor exceeds threshold"""
    
    def __init__(self, initial_size=8):
        self.size = initial_size
        self.count = 0
        self.load_factor_threshold = 0.7
        self.table = [[] for _ in range(self.size)]
    
    def hash_function(self, key):
        """Hash function"""
        return hash(key) % self.size
    
    def _resize(self):
        """Resize the table when load factor is exceeded"""
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        
        for bucket in old_table:
            for key, value in bucket:
                self.insert(key, value)
    
    def insert(self, key, value):
        """Insert with automatic resizing"""
        index = self.hash_function(key)
        
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        
        self.table[index].append((key, value))
        self.count += 1
        
        # Check load factor
        if self.count / self.size > self.load_factor_threshold:
            self._resize()
    
    def search(self, key):
        """Search for key"""
        index = self.hash_function(key)
        
        for k, v in self.table[index]:
            if k == key:
                return v
        
        return None
    
    def delete(self, key):
        """Delete key"""
        index = self.hash_function(key)
        
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                self.count -= 1
                return True
        
        return False


# ============================================================================
# 4. COMPLEX HASH TABLE - With Custom Objects and Advanced Features
# ============================================================================

class Student:
    """Example class for storing in hash table"""
    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa
    
    def __repr__(self):
        return f"Student({self.id}, {self.name}, {self.gpa})"


class AdvancedHashTable:
    """Advanced hash table with statistics and custom key handling"""
    
    def __init__(self, size=16):
        self.size = size
        self.table = [[] for _ in range(self.size)]
        self.count = 0
        self.collisions = 0
    
    def hash_function(self, key):
        """Support both hashable and custom objects"""
        if isinstance(key, str):
            return sum(ord(c) for c in key) % self.size
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert with collision tracking"""
        index = self.hash_function(key)
        
        # Check if bucket already has items (collision)
        if self.table[index]:
            self.collisions += 1
            for i, (k, v) in enumerate(self.table[index]):
                if k == key:
                    self.table[index][i] = (key, value)
                    return
        
        self.table[index].append((key, value))
        self.count += 1
    
    def search(self, key):
        """Search with validation"""
        index = self.hash_function(key)
        
        for k, v in self.table[index]:
            if k == key:
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def delete(self, key):
        """Delete with validation"""
        index = self.hash_function(key)
        
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index].pop(i)
                self.count -= 1
                return v
        
        raise KeyError(f"Key '{key}' not found")
    
    def get_stats(self):
        """Get hash table statistics"""
        return {
            'size': self.size,
            'entries': self.count,
            'collisions': self.collisions,
            'load_factor': self.count / self.size,
            'avg_chain_length': self.count / self.size
        }


# ============================================================================
# USAGE EXAMPLES
# ============================================================================

if __name__ == "__main__":
    print("=" * 70)
    print("1. SIMPLE HASH TABLE")
    print("=" * 70)
    simple_ht = SimpleHashTable(10)
    simple_ht.insert("apple", 5)
    simple_ht.insert("banana", 3)
    simple_ht.insert("orange", 7)
    print(f"Search 'apple': {simple_ht.search('apple')}")
    print(f"Search 'banana': {simple_ht.search('banana')}")
    simple_ht.delete("banana")
    print(f"After delete 'banana': {simple_ht.search('banana')}")
    
    print("\n" + "=" * 70)
    print("2. CHAINING HASH TABLE")
    print("=" * 70)
    chain_ht = ChainingHashTable(5)
    chain_ht.insert("name", "John")
    chain_ht.insert("age", 25)
    chain_ht.insert("city", "NYC")
    print(f"Search 'name': {chain_ht.search('name')}")
    print(f"Search 'age': {chain_ht.search('age')}")
    chain_ht.delete("age")
    print(f"After delete 'age': {chain_ht.search('age')}")
    
    print("\n" + "=" * 70)
    print("3. DYNAMIC HASH TABLE (Auto-resizing)")
    print("=" * 70)
    dyn_ht = DynamicHashTable(initial_size=4)
    for i in range(10):
        dyn_ht.insert(f"key{i}", f"value{i}")
    print(f"Final table size: {dyn_ht.size}")
    print(f"Search 'key5': {dyn_ht.search('key5')}")
    print(f"Search 'key9': {dyn_ht.search('key9')}")
    
    print("\n" + "=" * 70)
    print("4. ADVANCED HASH TABLE WITH CUSTOM OBJECTS")
    print("=" * 70)
    adv_ht = AdvancedHashTable()
    
    # Store Student objects
    students = [
        Student(101, "Alice", 3.8),
        Student(102, "Bob", 3.5),
        Student(103, "Charlie", 3.9),
    ]
    
    for student in students:
        adv_ht.insert(student.id, student)
    
    print(f"Search ID 102: {adv_ht.search(102)}")
    print(f"Delete ID 102: {adv_ht.delete(102)}")
    print(f"Table Stats: {adv_ht.get_stats()}")
