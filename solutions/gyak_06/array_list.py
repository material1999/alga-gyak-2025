######################
##### Array List #####
######################

import array

class ArrayList:
    def __init__(self):
        # 'i' means integer array; could also use 'f' for float, etc.
        self._data = array.array('i')

    def add(self, value):
        """Append a value to the end of the ArrayList."""
        self._data.append(value)

    def delete(self, index):
        """Delete an element at a given index."""
        if index < 0 or index >= len(self._data):
            print("Index out of range.")
            return
        del self._data[index]

    def get(self, index):
        """Get an element by index."""
        if index < 0 or index >= len(self._data):
            print("Index out of range.")
            return None
        return self._data[index]

    def size(self):
        """Return the number of elements."""
        return len(self._data)

    def display(self):
        """Print all elements."""
        print(list(self._data))

    def __repr__(self):
        return str(list(self._data))


# Example usage:
arr = ArrayList()
arr.add(10)
arr.add(20)
arr.add(30)
arr.display()      # [10, 20, 30]

arr.delete(1)
arr.display()      # [10, 30]

print(arr.get(0))  # 10
print("Size:", arr.size())  # Size: 2
