# email = input("What's your email? ").strip()

# a genaral idea to check for valid email
# if "@" in email and "." in email:
#    print("Valid")
# else:
#    print("Invalid")


# a more better way
# username, domain = email.split("@")
# if (username) and "." in domain:
#    print("Valid")
# else:
#    print("Invalid")

# a even better way
# username, domain = email.split("@")
# if (username) and domain.endswith(".com" or ".net" or ".org" or ".edu" or ".gov" or ".mil"):
#    print("Valid")
# else:
#    print("Invalid")


# a even better way usinf 're' library
import re
email = input("What's your email? ").strip()

# if re.search(".*@.*", email):
# if re.search(r"^[^@]+@[^@]+\.edu$", email):
# if re.search(r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9_]+\.edu$", email):
# if re.search(r"^\w+@\w+\.(edu|com|net|org|gov|mil)$", email, re.IGNORECASE): # \w = [a-zA-Z0-9_] not a . included
if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|net|org|gov|mil)$", email, re.IGNORECASE):  
   print("Valid")
else:
   print("Invalid")

#regular expression for most case [a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9]?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$
