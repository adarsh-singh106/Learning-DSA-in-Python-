import ctypes

class MeraList:
    """
    A custom implementation of a dynamic array (like Python's list)
    with efficient, industry-standard algorithms.
    """
    def __init__(self):
        self.size = 1  # The allocated capacity of the array
        self.n = 0     # The number of elements currently in the list

        # Create a C-Type Array with initial capacity = self.size
        self.A = self.make_my_array(self.size)

    def make_my_array(self, capacity):
        """Creates a C-Type array (static, referential) with a given capacity."""
        return (capacity * ctypes.py_object)()

    def __len__(self):
        """Returns the number of elements in the list. O(1)"""
        return self.n

    def append(self, item):
        """Appends an item to the end of the list. Amortized O(1)"""
        if self.size == self.n:
            # If the array is full, double its capacity
            self.resize(self.size * 2)
        
        # Append the item and increment the element count
        self.A[self.n] = item
        self.n += 1

    def resize(self, new_capacity):
        """Resizes the internal array to a new capacity. O(n)"""
        # Create a new array with the new capacity
        B = self.make_my_array(new_capacity)
        self.size = new_capacity

        # Copy elements from the old array to the new one
        for i in range(self.n):
            B[i] = self.A[i]
        
        # Replace the old array with the new one
        self.A = B

    # === EFFICIENT VERSION of __str__ ===
    def __str__(self):
        """Returns a string representation of the list. O(n)"""
        if self.n == 0:
            return '[]'
        # Using str.join() is O(n) and highly efficient.
        # String concatenation in a loop ("result = result + ...") is O(n^2).
        items = [str(self.A[i]) for i in range(self.n)]
        return '[' + ', '.join(items) + ']'

    def __getitem__(self, index):
        """Returns the item at the given index. O(1)"""
        if not (0 <= index < self.n):
            # It's standard to raise an IndexError, not return a string.
            raise IndexError("Index out of range")
        return self.A[index]

    def pop(self):
        """Removes and returns the last item from the list. O(1)"""
        if self.n == 0:
            raise IndexError("pop from empty list")
        
        # A standard pop returns the item that was removed.
        item = self.A[self.n - 1]
        self.n -= 1
        return item

    def clear(self):
        """Removes all items from the list. O(1)"""
        self.n = 0
        self.size = 1
        self.A = self.make_my_array(self.size)

    def find(self, item):
        """
        Finds the index of the first occurrence of an item. O(n)
        Raises ValueError if the item is not found.
        """
        for i in range(self.n):
            if item == self.A[i]:
                return i
        # It's standard to raise a ValueError, similar to list.index().
        raise ValueError(f"'{item}' is not in list")

    def insert(self, pos, item):
        """Inserts an item at a given position. O(n)"""
        if not (0 <= pos <= self.n):
            raise IndexError("Index out of range")
            
        if self.n == self.size:
            self.resize(self.size * 2)

        # Shift elements to the right of the position
        for i in range(self.n, pos, -1):
            self.A[i] = self.A[i - 1]

        # Insert the item and increment element count
        self.A[pos] = item
        self.n += 1

    def __delitem__(self, pos):
        """Deletes an item at a given position. O(n)"""
        if not (0 <= pos < self.n):
            raise IndexError("Index out of range")

        # Shift elements to the left to overwrite the deleted item
        for i in range(pos, self.n - 1):
            self.A[i] = self.A[i + 1]
        
        self.n -= 1
    
    def remove(self, item):
        """Removes the first occurrence of an item. O(n)"""
        try:
            pos = self.find(item)
            self.__delitem__(pos)
        except ValueError:
            # Propagate the ValueError if the item is not found
            raise ValueError(f"'{item}' is not in list")

    # === EFFICIENT VERSION of sort ===
    def sort(self, reverse=False):
        """
        Sorts the list in-place using an efficient algorithm. O(n log n)
        """
        # The most practical and "industry-level" way is to leverage Python's
        # own highly optimized Timsort algorithm.
        
        # 1. Extract elements to a temporary Python list
        temp_list = [self.A[i] for i in range(self.n)]
        
        # 2. Sort the temporary list (O(n log n))
        temp_list.sort(reverse=reverse)
        
        # 3. Copy the sorted elements back to our array
        for i in range(self.n):
            self.A[i] = temp_list[i]

    # === EFFICIENT VERSION of min ===
    def min(self):
        """Returns the minimum item in the list. O(n)"""
        if self.n == 0:
            raise ValueError("min() arg is an empty sequence")
        
        # This is an O(n) operation, vastly more efficient than sorting.
        min_val = self.A[0]
        for i in range(1, self.n):
            if self.A[i] < min_val:
                min_val = self.A[i]
        return min_val
        
    # === EFFICIENT VERSION of max ===
    def max(self):
        """Returns the maximum item in the list. O(n)"""
        if self.n == 0:
            raise ValueError("max() arg is an empty sequence")
            
        # This is an O(n) operation.
        max_val = self.A[0]
        for i in range(1, self.n):
            if self.A[i] > max_val:
                max_val = self.A[i]
        return max_val
    
    def sum(self):
        """Returns the sum of all items in the list. O(n)"""
        total = 0
        for i in range(self.n):
            total += self.A[i]
        return total
    
    def extend(self, other_iterable):
        """Extends the list by appending all items from an iterable. O(k) where k is len(other_iterable)"""
        other_list = list(other_iterable) # Ensure it's a sequence with a length
        m = len(other_list)
        
        # Resize once if needed, calculating the required capacity first
        required_capacity = self.n + m
        if self.size < required_capacity:
            new_capacity = self.size
            while new_capacity < required_capacity:
                new_capacity *= 2
            self.resize(new_capacity)

        # Copy new elements directly
        for i in range(m):
            self.A[self.n] = other_list[i]
            self.n += 1


# --- Example Usage ---

l = MeraList()
l.append(10)
l.append(50)
l.append(5)
l.append(100)
l.append(25)

print(f"Original List: {l}")
print(f"Length: {len(l)}")

# Test efficient min() and max()
print(f"Min value: {l.min()}")  # Should be 5
print(f"Max value: {l.max()}")  # Should be 100

# Test efficient sort()
l.sort()
print(f"Sorted List: {l}")

l.sort(reverse=True)
print(f"Reverse Sorted List: {l}")

# Test pop() and __getitem__()
popped_item = l.pop()
print(f"Popped item: {popped_item}") # Should be 5
print(f"List after pop: {l}")
print(f"Item at index 1: {l[1]}") # Should be 25

# Test extend()
another_list = [1, 2, 3]
l.extend(another_list)
print(f"List after extend: {l}")

# Test error handling
try:
    l.find(999)
except ValueError as e:
    print(f"Caught expected error: {e}")

try:
    print(l[100])
except IndexError as e:
    print(f"Caught expected error: {e}")