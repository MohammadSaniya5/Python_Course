# List Methods

numbers = [10, 20, 30]

numbers.append(40)       # Add element at end
print("After append:", numbers)

numbers.insert(1, 15)    # Insert at index
print("After insert:", numbers)

numbers.remove(20)       # Remove element
print("After remove:", numbers)

numbers.pop()            # Remove last element
print("After pop:", numbers)

numbers.sort()           # Sort list
print("After sort:", numbers)

numbers.reverse()        # Reverse list
print("After reverse:", numbers)

print("Count of 30:", numbers.count(30))
