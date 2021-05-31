from setup import *
from utils import to_str

def print_max_fitness(pop, goal):
    pop.sort(key = lambda a: - a.fitness(goal))

    print(
        to_str(pop[0].dna.guess),
        pop[0].dna.cultural,
        pop[0].fitness(goal)
    )

    print(to_str(goal))

def debug(pop, goal):
    s = sum([a.dna.cultural for a in pop])

    cult_fit = sum([a.fitness(goal) if a.dna.cultural else 0 for a in pop])
    hard_fit = sum([a.fitness(goal) for a in pop]) - cult_fit

    cult_num = sum([a.dna.cultural for a in pop])
    hard_num = pop_size - cult_num

    cult_avg_fit = cult_fit / cult_num if cult_num != 0 else 0
    hard_avg_fit = hard_fit / hard_num if hard_num != 0 else 0

    print(f'{round(cult_avg_fit, 2)}\t{round(hard_avg_fit, 2)}\t{s}')

    # Max fitness
    # print_max_fitness(pop, goal)

def season_debug(pop, goal):
    print('\nNew season!')

    # Max fitness
    # print_max_fitness(pop, goal)
