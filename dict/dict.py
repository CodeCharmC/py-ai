
# Creating a simple dictionary
student = {"name": "Alice", "age": 22, "course": "Computer Science"}
print(student)

# Access value by key
print(student["name"])  # Output: Alice
print(student["age"])   # Output: 22

# Adding a new key-value pair
student["graduation_year"] = 2024

# Updating an existing key-value pair
student["age"] = 23
print(student)

# Using del to remove a key-value pair
del student["course"]

# Using pop() to remove a key-value pair and return the value
graduation_year = student.pop("graduation_year")
print(graduation_year)  # Output: 2024
print(student)

if "name" in student:
    print("Name is in the dictionary!")

if "course" not in student:
    print("Course is not in the dictionary!")

# Looping through keys
for key in student:
    print(key)

# Looping through keys and values
for key, value in student.items():
    print(key, ":", value)
