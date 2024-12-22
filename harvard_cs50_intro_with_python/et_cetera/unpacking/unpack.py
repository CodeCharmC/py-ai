
# enample of unpacking frist name from a name
frist, _ = input("What's your name? ").split(" ")
print(f"Hello {frist}")

def total(galloons, sickles, knuts):
   return galloons * 17 + sickles * 29 + knuts

#normaly
print(total(100, 50, 25), "knuts")

#or lest's say we have a list
coins = [100, 50, 25]
print(total(coins[0], coins[1], coins[2]), "knuts") #one way
print(total(*coins), "knuts") #another way

#or we have a dictionary
coins = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "knuts") #one way
print(total(**coins), "knuts") #another way