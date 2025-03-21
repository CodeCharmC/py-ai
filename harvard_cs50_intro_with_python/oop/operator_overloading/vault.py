class Vault:
   def __init__(self, galleons=0, sickles=0, knuts=0):
      self.galleons = galleons
      self.sickles = sickles
      self.knuts = knuts

   def __str__(self):
      return f"{self.galleons}g {self.sickles}s {self.knuts}k"
   
   def __add__(self, other):
      galleons = self.galleons + other.galleons
      sickles = self.sickles + other.sickles
      knuts = self.knuts + other.knuts
      return Vault(galleons, sickles, knuts)
   
potter = Vault(100, 50, 25)
print(potter)

severus = Vault(25, 10, 5)
print(severus)


# galleons = potter.galleons + severus.galleons
# sickles = potter.sickles + severus.sickles
# knuts = potter.knuts + severus.knuts
# total = Vault(galleons, sickles, knuts)

#alternative     
total = potter + severus

print(total)