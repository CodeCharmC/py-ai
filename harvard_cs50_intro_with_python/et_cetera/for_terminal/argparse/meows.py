import argparse

parser = argparse.ArgumentParser(description="Meow n times.")
parser.add_argument("-n", help="Number of meows", type=int, default=1)
args = parser.parse_args()

for _ in range(int(args.n)):
   print("meow")

#in terminal

# python meows.py
#output
# meow

# python meows.py -n 3
# output
# meow
# meow
# meow