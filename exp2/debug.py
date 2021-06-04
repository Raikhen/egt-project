from setup import *
from utils import to_str, hamming_fitness

def print_max_fitness(pop, goal):
    pop.sort(key = lambda a: - a.fitness(goal))

    print(
        to_str(pop[0].dna.guess),
        pop[0].dna.cultural,
        pop[0].fitness(goal)
    )

    print(to_str(goal))

def debug(pop, gen, goal):
    # Only cultured agents
    cultured = list(filter(lambda a: a.dna.cultural, pop))

    # Sum of fitness of cultured and genetic agents
    cult_fit = sum([a.fitness(goal) for a in cultured])
    hard_fit = sum([a.fitness(goal) for a in pop]) - cult_fit

    # Number of cultured and genetic agents
    cult_num = len(cultured)
    hard_num = pop_size - cult_num

    # Average fitness for cultured and genetic agents
    cscore = round(cult_fit / cult_num, 3) if cult_num != 0 else 0
    gscore = round(hard_fit / hard_num, 3) if hard_num != 0 else 0

    # Frequency of cultured in the population
    cdom = round(cult_num / pop_size, 3)

    # Season
    season = gen // season_len

    # Only hardcoders
    hardcoders = list(filter(lambda a: not a.dna.cultural, pop))
    memes = [h.meme for h in hardcoders]
    avg = sum([hamming_fitness(m, goal) for m in memes]) / len(hardcoders)
    avg = round(avg, 3)

    print(f'{season}\t{gen}\t{cscore}\t{gscore}\t{cdom}\t{avg}')
