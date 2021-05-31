import numpy as np

from setup import *

class DNA:
    def __init__(self):
        self.guess = np.random.choice([0, 1], size = str_len)
        # self.culture_weight = np.random.random()
        # self.brain = Brain()

    def mutate(self):
        for i in range(str_len):
            if np.random.random() < dna_mut_rate:
                self.guess[i] = 1 - self.guess[i]

    def __repr__(self):
        return ''.join([str(e) for e in self.guess])
