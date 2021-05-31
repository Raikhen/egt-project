import numpy as np

from setup import *
from agent import Agent

# Span population
pop = [Agent() for _ in range(pop_size)]

goal = [1] * str_len

for gen in range(gens):
    s = sum([pop[i].fitness(goal) for i in range(pop_size)])
    p = [pop[i].fitness(goal) / s for i in range(pop_size)]

    print(pop[0], round(s / pop_size, 2))

    # Selection
    to_repr = np.random.choice(range(pop_size), p = p)
    to_kill = np.random.choice(range(pop_size))

    # Replacement
    new = pop[to_repr].reproduce()
    pop[to_kill] = new
