balance = 0

def main():
   print(f"Balance: ${balance}")
   deposit(100)
   withdraw(50)
   print(f"New Balance: ${balance}")

def deposit(amount):
   global balance 
   balance += amount

def withdraw(amount):
   global balance
   balance -= amount

if __name__ == "__main__":
   main()