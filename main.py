import numpy as np

from agent import Agent

# Parameters
pop_size = 50
gens_qty = 100

pop = [Agent() for _ in range(pop_size)]

for i in range(gens_qty):
    # learning period
    # clean worse (death)
    # reproduce leftover (reproduction)
    return
