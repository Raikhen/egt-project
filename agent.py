import random

from meme       import Meme
from copying    import mutate, get_copying, random_polynomial

# Parameters
meme_qty = 10

class Agent:
    def __init__(self, dna = random_polynomial()):
        self.dna = mutate(dna)
        self.copying = get_copying(self.dna)
        self.memes = [Meme() for _ in range(meme_qty)]

    def fitness(self):
        return sum([m.fitness() for m in self.memes])

    def reproduce(self):
        return Agent(self.dna)
