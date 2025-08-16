# Useful String Methods
text = "  Python Programming Language  "

print(len(text))               # Length of string
print(text.strip())            # Remove spaces
print(text.lower())            # Lowercase
print(text.upper())            # Uppercase
print(text.title())            # Each word capitalized
print(text.capitalize())       # First letter capitalized
print(text.find("gram"))       # Find substring
print(text.count("m"))         # Count occurrences
print(text.replace("Python", "Java")) # Replace words
print("Python" in text)        # Check substring
print(text.split())            # Split into list
print("-".join(["Python", "Java", "C++"])) # Join list into string
