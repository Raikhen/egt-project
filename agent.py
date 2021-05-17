import math
import random
import sympy

from copying import get_copying, random_polynomial

# Parameters
meme_qty = 10

class Agent:
    def __init__(self):
        self.dna = random_polynomial()
        self.copying = get_copying(self.dna)
        self.memes = [Meme() for _ in range(meme_qty)]

    def fitness(self):
        return sum([m.fitness() for m in self.memes])
