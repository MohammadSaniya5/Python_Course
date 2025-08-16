# Simple List Examples

# Example 1: Sum of list elements
numbers = [10, 20, 30, 40]
print("Sum:", sum(numbers))

# Example 2: Find maximum and minimum
print("Max:", max(numbers))
print("Min:", min(numbers))

# Example 3: Check if an element exists
print("Is 20 in numbers?", 20 in numbers)
print("Is 50 in numbers?", 50 in numbers)

# Example 4: Remove duplicates
nums = [1, 2, 2, 3, 4, 4, 5]
unique = list(set(nums))
print("Unique numbers:", unique)

# Example 5: List comprehension
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)
