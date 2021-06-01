import numpy as np

from setup import *
from debug import debug
from agent import Agent
from utils import hamming_fitness

# Span population
pop = [Agent() for _ in range(pop_size)]

# Set goal
goal = [1] * str_len

for gen in range(gens):
    # Season management
    if gen % season_len == 0:
        goal = np.random.choice([0, 1], size = str_len)

    debug(pop, gen, goal)

    # Exploratory time
    for a in pop:
        for j in range(expl_attempts):
            attempt = np.random.choice([0, 1], size = str_len)

            attempt_fitness = hamming_fitness(attempt, goal)
            your_fitness    = hamming_fitness(a.meme, goal)

            if attempt_fitness > your_fitness:
                a.meme = attempt

    # Copying seasons
    for i in range(copy_num):
        copier = np.random.choice(pop)
        copied = np.random.choice(pop)
        copier.copies(copied, goal)

    # Fitness and reproduction probabilities
    s = sum([pop[i].fitness(goal) for i in range(pop_size)])
    p = [pop[i].fitness(goal) / s for i in range(pop_size)]

    # Debug
    debug(pop, gen, goal)

    # Selection
    to_repr = np.random.choice(range(pop_size), p = p)
    to_kill = np.random.choice(range(pop_size))

    # Replacement
    new = pop[to_repr].reproduce()
    pop[to_kill] = new
