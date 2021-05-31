import numpy as np

from setup import *
from utils import to_str

class DNA:
    def __init__(self):
        self.guess = np.random.choice([0, 1], size = str_len)
        self.cultural = np.random.choice([True, False])

        # Copying evaluation function
        m = np.random.uniform(-1, 1)
        b = np.random.uniform(-1, 1)
        self.eval_data = (m, b)

    def mutate(self):
        # Guess
        for i in range(str_len):
            if np.random.random() < dna_mut_rate:
                self.guess[i] = 1 - self.guess[i]

        # Is cultural
        if np.random.random() < is_cultural_mut_rate:
            self.cultural = not self.cultural

        # Copying function
        m, b = self.eval_data
        new_m = np.clip(np.random.normal(m, copy_mut), -1, 1)
        new_b = np.clip(np.random.normal(b, copy_mut), -1, 1)
        self.eval_data = (new_m, new_b)

    def __repr__(self):
        guess = to_str(self.guess)
        return str((guess, self.cultural, self.eval_data))
