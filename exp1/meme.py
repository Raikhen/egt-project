import math
import sympy
import random

# Parameters
meme_min = 1
meme_max = 1
mut_rate = 0.1
mut_min = -10
mut_max = 10

class Meme:
    def __init__(self, n = -1):
        self.n = n if n != -1 else random.randint(meme_min, meme_max)

    def fitness(self):
        ind = 1 if sympy.isprime(self.n) else 0
        return ind * (self.n / (1 + self.n)) ** 2

    def mutate(self):
        if random.uniform(0, 1) > mut_rate:
            new = self.n + random.randint(mut_min, mut_max)

            '''
            if random.uniform(0, 1) > .999:
                print(f'mutating meme from {self.n} to {new}')
            '''

            return Meme(new)

        return Meme(self.n)

    def __repr__(self):
        return f'{self.n}'
