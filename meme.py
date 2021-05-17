import random

# Parameters
meme_min = 1
meme_max = 10

class Meme:
    def __init__(self, n = -1):
        self.n = n if n != -1 else random.randint(meme_min, meme_max)

    def fitness(self):
        return 1 + math.log(self.n) if sympy.isprime(self.n) else 0
