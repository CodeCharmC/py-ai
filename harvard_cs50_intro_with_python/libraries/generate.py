# one way to import random
# import random
# coin = random.choice(["heads", "tails"])
# print(coin)

# another way to import random   
# from random import choice
# coin = choice(["heads", "tails"])
# print(coin)


# random randint
# import random
# n = random.randint(1, 10)
# print(n)


import random
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
   print(card)
