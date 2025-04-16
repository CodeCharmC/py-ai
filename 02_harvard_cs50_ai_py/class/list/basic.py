fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[2])  # Output: cherry

fruits[1] = "orange"
print(fruits)  # ['apple', 'orange', 'cherry']

fruits.append("grape")  # adds to the end
print(fruits)

fruits.remove("apple")  # removes the first match
print(fruits)

for fruit in fruits:
   print(fruit)
   
if "cherry" in fruits:
   print("Yay! 🍒 is in the list")
