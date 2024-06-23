# Create an empty set using the constructor method.
numbers = set() 
print(numbers) # Output: set()
# Note: {} creates a dictionary in Python.
print(type({})) # Output: <class 'dict'>

# set() constructor function takes an iterable as input.
numbers = set([1, 2])
print(numbers) # Output: {1, 2}
string_set = set("hello")
print(string_set) # Output: {'o', 'e', 'l', 'h'}

# Sets with some elements can also be created using {}.
numbers = {1, 2, 1, 2, 3, 5}
print(numbers) # Output: {1, 2, 3, 5}

# Set contains only unique elements. But they can contain elements of different types.
random_set = {'a', 'a', 1, 2, 1}
print(random_set) # Output: {1, 2, 'a'}

# Sets can contain only hashable elements.
# Sets cannot contain other sets.
my_set = {1, 2}
set_to_add = {3, 4}
my_set.add(set_to_add) # Raises "TypeError: unhashable type: 'set'"
# To create set of sets, use a frozenset
my_set.add(frozenset(set_to_add))
print(my_set) # Output: {1, 2, frozenset({3, 4})}

# Length of a set.
numbers = {1, 2, 3}
print(len(numbers)) # Output: 3

# Check if an element is in a set using 'in'
print(1 in {1, 2, 3}) # Output: True
print(5 in {1, 2, 3}) # Output: False
print(1 not in {1, 2, 3}) # Output: False

# Access elements in a set
numbers = {1, 2, 3}
for number in numbers:
    print(number)

# Union: Elements in either set_1, set_2 or both.
set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}
print(set_1.union(set_2)) # Output: {1, 2, 3, 4, 5, 6}
print(set_1 | set_2) # Output: {1, 2, 3, 4, 5, 6}

# Intersection: Elements in both set_1 and set_2
set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}
print(set_1.intersection(set_2)) # Output: {3, 4}
print(set_1 & set_2) # Output: {3, 4}

# Set difference: Elements in set_1 not in set_2
set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}
print(set_1.difference(set_2)) # Output: {1, 2}
print(set_1 - set_2) # Output: {1, 2}

# Symmetric difference: Elements in set_1 or set_2, but not in both.
set_1 = {1, 2, 3, 4}
set_2 = {3, 4, 5, 6}
print(set_1.symmetric_difference(set_2)) # Output: {1, 2, 5, 6}
print(set_1 ^ set_2) # Output: {1, 2, 5, 6}

# Check if a set is a subset of another.
set_1 = {1, 2}
set_2 = {1, 2, 3}
print(set_1.issubset(set_2)) # Output: True
print(set_2.issubset(set_1)) # Output: False

# Check if a set is a superset of another.
set_1 = {1, 2}
set_2 = {1, 2, 3}
print(set_1.issuperset(set_2)) # Output: False
print(set_2.issuperset(set_1)) # Output: True

# Add one element to set using add() methd.
numbers = {1, 2, 3}
numbers.add(4) # <- takes a single hashable element.
print(numbers) # Output: {1, 2, 3, 4}

# Add multiple elements to set using update() methd.
numbers = {1, 2, 3}
numbers.update([4, 5]) # <- takes any iterable.
print(numbers) # Output: {1, 2, 3, 4, 5}

# Remove elements using remove() method.
numbers = {1, 2, 3}
numbers.remove(1)
print(numbers) # Output: {2, 3}
numbers.remove(5) # Raises KeyError if element is not present.

# Remove elements using discard element.
numbers = {1, 2, 3}
numbers.discard(1)
print(numbers) # Output: {2, 3}
numbers.discard(5) # Does not raise any error even if element is not present.

# Remove and get the last item in a set, sets are unordered so any element could get removed!
numbers = {1, 2, 3}
print(numbers.pop()) # Output: 3
print(numbers) # Output: {1, 2}

# Empty set using clear()
numbers = {1, 2, 3}
numbers.clear()
print(numbers) # Output: set()

# Delete set using del keyword
numbers = {1, 2}
del numbers