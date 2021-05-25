import random

from dna        import DNA
from meme       import Meme

# Parameters
meme_qty = 10

class Agent:
    def __init__(self, dna = -1):
        self.dna = DNA(dna)
        self.copying = self.dna.get_copying()
        self.memes = [Meme() for _ in range(meme_qty)]

    def fitness(self):
        return sum([m.fitness() for m in self.memes]) / meme_qty

    def reproduce(self):
        return Agent(self.dna)
