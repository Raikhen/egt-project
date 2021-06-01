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

def debug(pop, gen, goal):
    cultured = list(filter(lambda a: a.dna.cultural, pop))

    cult_fit = sum([a.fitness(goal) for a in cultured])
    hard_fit = sum([a.fitness(goal) for a in pop]) - cult_fit

    cult_num = len(cultured)
    hard_num = pop_size - cult_num

    cult_avg_fit = cult_fit / cult_num if cult_num != 0 else 0
    hard_avg_fit = hard_fit / hard_num if hard_num != 0 else 0

    print(f'{round(cult_avg_fit, 2)}\t{round(hard_avg_fit, 2)}\t{cult_num}')

    # print(cultured[0].dna.eval_data)

    # Max fitness
    # print_max_fitness(pop, goal)
