import random
import sympy

# Parameters
meme_qty = 10
poly_deg = 5
poly_min = -2
poly_max = 2
meme_min = 1
meme_max = 10

class Agent:
    def __init__(self):
        self.dna = random_polynomial()
        self.memes = []

        for _ in range(meme_qty):
            self.memes.append(random.randint(meme_min, meme_max))

    def fitness(self):
        return sum([1 if sympy.isprime(m) else 0 for m in self.memes])
