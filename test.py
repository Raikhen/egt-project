import numpy as np
from collections import Counter

def test(pop, iter):
    pop_size = len(pop)

    pop.sort(key = lambda a: - a.fitness())

    avg_f = sum([a.fitness() for a in pop]) / pop_size
    new_f = 2 * sum([a.fitness() for a in pop[pop_size // 2:]]) / pop_size
    min_f = pop[-1].fitness()
    max_f = pop[0].fitness()

    meme_pop = np.matrix([a.memes for a in pop]).flatten()
    meme_pop = np.squeeze(np.asarray(meme_pop)).tolist()
    meme_pop = [f'{m}' for m in meme_pop]
    meme_count = Counter(meme_pop).most_common(5)

    print(
        f'''Iteration {iter}
        new {round(new_f, 2)} \t
        avg {round(avg_f, 2)} \t
        min {round(min_f, 2)} \t
        max {round(max_f, 2)} \t
        max {pop[0].memes} \t
        min {pop[-1].memes} \t
        max_learner {pop[pop_size // 2:][0].memes} \t
        {meme_count}'''
    )
