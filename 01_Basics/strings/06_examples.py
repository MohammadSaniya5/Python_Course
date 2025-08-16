# Simple String Examples in Python

# Example 1: Joining first and last name
first_name = "Mohammad"
last_name = "Saniya"
full_name = first_name + " " + last_name
print("Full Name:", full_name)

# Example 2: Checking if a word exists in a sentence
sentence = "Python is a powerful language"
print("Does sentence contain 'Python'? ->", "Python" in sentence)
print("Does sentence contain 'Java'? ->", "Java" in sentence)

# Example 3: Counting characters in a string
word = "programming"
print("Length of word:", len(word))
print("Number of 'm':", word.count("m"))

# Example 4: Changing case
text = "hello world"
print("Uppercase:", text.upper())
print("Title Case:", text.title())

# Example 5: Splitting a sentence into words
sentence = "I love learning Python"
words = sentence.split()
print("Words:", words)

# Example 6: Replacing a word
new_sentence = sentence.replace("Python", "Java")
print("After replacement:", new_sentence)

# Example 7: Reversing a string
word = "Python"
print("Reversed:", word[::-1])

# Example 8: Palindrome check (same forward and backward)
word = "madam"
if word == word[::-1]:
    print(word, "is a Palindrome")
else:
    print(word, "is NOT a Palindrome")
