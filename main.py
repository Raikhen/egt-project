import random

from test   import test
from agent  import Agent

# Parameters
pop_size = 50
gens_qty = 1000
copy_qty = 40

pop = [Agent() for _ in range(pop_size)]

for j in range(gens_qty):
    # Learning Phase
    for a in pop:
        for i, m in enumerate(a.memes):
            to_copy = random.sample(pop, copy_qty)

            for b in to_copy:
                amf = m.fitness() # The fitness of the meme in agent a
                bmf = b.memes[i].fitness() # The fitness of the meme in agent b
                p = a.copying(amf, bmf)

                if random.uniform(0, 1) > p:
                    a.memes[i] = b.memes[i].mutate()

    # Testing
    test(pop, j)

    # Survival Phase
    pop.sort(key = lambda a: - a.fitness())
    pop = pop[:pop_size // 2]

    # Reproduction Phase
    pop += [a.reproduce() for a in pop]
