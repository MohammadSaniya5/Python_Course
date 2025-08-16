# Tuple Unpacking

person = ("Mohammad", 21, "Student")

name, age, role = person
print("Name:", name)
print("Age:", age)
print("Role:", role)

# Using * to unpack multiple values
numbers = (1, 2, 3, 4, 5)
a, b, *rest = numbers
print("a:", a)
print("b:", b)
print("rest:", rest)
