class Account:
   def __init__(self):
      self._balance = 0   #_balance means its a private variable also known as instance variable
      #instance variable is accessible  to all the methods of the class because we are accessing it using the special parameter 'self'
   @property
   def balance(self):
      return self._balance
   
   def deposit(self, amount):
      self._balance += amount

   def withdraw(self, amount):
      self._balance -= amount


def main():
   account = Account()
   print(f"Balance: ${account.balance}")
   account.deposit(100)
   account.withdraw(50)
   print(f"New Balance: ${account.balance}")


if __name__ == "__main__":
   main()