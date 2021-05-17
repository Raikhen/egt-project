import random

from agent import Agent

# Parameters
pop_size = 50
gens_qty = 100
copy_qty = 5

pop = [Agent() for _ in range(pop_size)]
print(pop[0].copying(0.0001, 0.0004))

# learning period
# clean worse (death)
# reproduce leftover (reproduction)

for i in range(gens_qty):
    # Learning Phase
    for a in pop:
        for i, m in enumerate(a.memes):
            to_copy = random.sample(pop, copy_qty)

            for b in to_copy:
                amf = m.fitness() # The fitness of the meme in agent a
                bmf = b.memes[i].fitness() # The fitness of the meme in agent b
                p = a.copying(amf, bmf)

                if random.uniform(0, 1) > p:
                    a.memes[i] = b.memes[i]

    # Survival Phase
    # ...

    # Reproduction Phase
    # ...
