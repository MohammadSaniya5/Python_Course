# Simple Tuple Examples

# Example 1: Swapping variables using tuple unpacking
a, b = 10, 20
print("Before Swap:", a, b)
a, b = b, a
print("After Swap:", a, b)

# Example 2: Returning multiple values from a function
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print("Coordinates:", x, y)

# Example 3: Using tuple in a loop
students = [("Alice", 20), ("Bob", 22), ("Charlie", 21)]
for name, age in students:
    print(f"{name} is {age} years old")
