import numpy as np
from copy import deepcopy

from setup  import *
from dna    import DNA
from utils  import mutate_meme, hamming_fitness

class Agent:
    def __init__(self, dna = -1):
        # Genetic
        if dna == -1:
            self.dna = DNA()
        else:
            self.dna = deepcopy(dna)

        # Copying evaluation function
        m, b = self.dna.eval_data
        self.evaluate = lambda x: m * x + b > 0

        # Cultural
        self.meme = np.random.choice([0, 1], size = str_len)

    def fitness(self, goal):
        c       = self.dna.cultural
        guess   = self.meme if c else self.dna.guess
        m       = 1 - brain_cost if c else 1

        return hamming_fitness(guess, goal) * m

    def reproduce(self):
        return Agent(self.dna)

    def __repr__(self):
        return str(self.dna)

    def copies(self, copied, goal):
        fitness_diff = self.fitness(goal) - copied.fitness(goal)

        if self.evaluate(fitness_diff):
            self.meme = mutate_meme(deepcopy(copied.meme))
