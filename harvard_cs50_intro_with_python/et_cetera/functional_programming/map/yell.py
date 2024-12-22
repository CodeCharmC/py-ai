#example 1
def main():
   yell("Hello world, how are you!")

def yell(phrase):
   print(phrase.upper())   

if __name__ == "__main__":
   main()

#----------------------------------------------------------

#example 2
def main():
   yell(["Hello", " world,", " how", " are", " you!"])

def yell(words):
   uppercased = []
   for word in words:
      uppercased.append(word.upper())
   print(*uppercased) #unpack 

if __name__ == "__main__":
   main()


#----------------------------------------------------------

#example 3
def main():
   yell("Hello", " world", "how", " are", " you", "!")

def yell(*words): #unpack
   uppercased = []
   for word in words:
      uppercased.append(word.upper())
   print(*uppercased) #unpack 

if __name__ == "__main__":
   main()


#----------------------------------------------------------

#example 4 --> using map         **** use of python functional programming ---map()
def main():
   yell("Hello", " world", "how", " are", " you", "!")

def yell(*words): #unpack
   uppercased = map(str.upper, words)
   print(*uppercased) #unpack 

if __name__ == "__main__":
   main()


#----------------------------------------------------------

#example 4 --> list comprehension
def main():
   yell("Hello", " world", "how", " are", " you", "!")

def yell(*words): #unpack
   uppercased = [word.upper() for word in words]
   print(*uppercased) #unpack 

if __name__ == "__main__":
   main()