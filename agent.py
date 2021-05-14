import random
import sympy

from copying import get_copying, random_polynomial

# Parameters
meme_qty = 10
meme_min = 1
meme_max = 10

class Agent:
    def __init__(self):
        self.dna = random_polynomial()
        self.copying = get_copying(self.dna)
        self.memes = []

        for _ in range(meme_qty):
            self.memes.append(random.randint(meme_min, meme_max))

    def fitness(self):
        return sum([1 if sympy.isprime(m) else 0 for m in self.memes])
