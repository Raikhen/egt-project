import numpy as np
from copy import deepcopy

from setup  import *
from dna    import DNA

class Agent:
    def __init__(self, dna = DNA()):
        self.dna = deepcopy(dna)
        self.dna.mutate()

    def fitness(self, goal):
        diff = np.logical_xor(self.dna.guess, goal)
        as_str = ''.join([str(int(e)) for e in diff])

        dist = sum(diff) / (2 * str_len)
        bonus = 0 if '01' in as_str else 0.5

        return (0.5 - dist) + bonus

    def reproduce(self):
        return Agent(self.dna)

    def __repr__(self):
        return str(self.dna)
