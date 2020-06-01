"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]
print(f"Original List: {a[:]}")

# Output the second element: 4:
print(f"Second Element: {a[1:2]}")

# Output the second-to-last element: 9
print(f"Second-to-last Element: {a[-2:-1]}")

# Output the last three elements in the array: [7, 9, 6]
print(f"Last three Elements: {a[-3:]}")

# Output the two middle elements in the array: [1, 7]
print(f"Two middle elements: {a[2:4]}")

# Output every element except the first one: [4, 1, 7, 9, 6]
print(f"All elements except index 0: {a[1::]}")

# Output every element except the last one: [2, 4, 1, 7, 9]
print(f"Every element except last one: {a[:-1]}")

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"
print(f"8-12th characters of \"Hello, world!\": {s[7:12]}")