def hello(to="world!"):
   print("Hello,", to)


print("What is your name?")
name = input().strip().title()

hello(name)



# print(input("What is your name? ").strip().title())


# print("Hello " + name)

# print(f"Hello {name}")

# print("Hello", name)


# print("Hello %s" % name)

# print("Hello {}".format(name))

# print("Hello", + name)
# TypeError: bad operand type for unary +: 'str'

# print("Hello ", name, sep="999", end="!" )  

# print("Hello", "'friend'")
# print("Hello", "\"friend\"")

# print("Hello", name)