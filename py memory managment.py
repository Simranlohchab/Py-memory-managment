class MyClass:
    def __init__(self, value):
        self.value = value
1) creating and deleting an object 
# Create an object
obj = MyClass(5)

# Print the object's value
print(obj.value)
# Output: 5

# Delete the object
del obj

# Attempting to access the object's value will result in an error
print(obj.value)
# Output: NameError: name 'obj' is not referenced

2)Using weak references:

import weakref

class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(5)

# Create a weak reference to the object
weak_obj = weakref.ref(obj)

# Print the object's value through the weak reference
print(weak_obj().value)
# Output: 5

# Delete the object
del obj

# Attempting to access the object's value through the weak reference will return None
print(weak_obj())
# Output: None


3)Using garbage collection:
import gc

class MyClass:
    def __init__(self, value):
        self.value = value

obj = MyClass(5)

# Print the object's value
print(obj.value)
# Output: 5

# Delete the object
del obj

# Collect unreferenced objects
gc.collect()

# The garbage collector will collect the unreferenced object and release its memory.


4)Using 'sys.getsizeof()':
import sys

obj = [i for i in range(1000)]

# get the size of the object
size = sys.getsizeof(obj)

print("The size of the object is", size, "bytes")
