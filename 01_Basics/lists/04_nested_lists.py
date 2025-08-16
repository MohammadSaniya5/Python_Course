# Nested Lists (Lists inside Lists)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:", matrix)
print("First row:", matrix[0])
print("Element at [1][2]:", matrix[1][2])

# Iterating through nested lists
for row in matrix:
    print("Row:", row)
