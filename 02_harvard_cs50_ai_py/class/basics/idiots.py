import random

class Idiots:
    def __init__(self, name, joke=None, reactions=None):
        self.name = name  # A name for your funny person
        self.joke = joke if joke else "Why don't skeletons fight each other? They don't have the guts!"  # Default joke
        self.reactions = reactions if reactions else [
            "Haha, that's hilarious!",
            "Oh no, not this one again!",
            "Groan... that was bad!",
            "I can't believe I laughed at that!"
        ]  # Default reactions

    def tell_joke(self):
        print(f"{self.name} says: {self.joke}")
        # Random reaction from the list
        print(f"Reaction: {random.choice(self.reactions)}")

funny_bob = Idiots("Bob", "Why do programmers prefer dark mode? Because the light attracts bugs!")
funny_alice = Idiots("Alice", "Why did the developer go broke? Because he used up all his cache!")
funny_Inn = Idiots("Inn", "Why do programmers always mix up Christmas and Halloween?Because Oct 31 == Dec 25!")


# Telling the jokes
funny_bob.tell_joke()
print() 
funny_alice.tell_joke()
print()
funny_Inn.tell_joke()

