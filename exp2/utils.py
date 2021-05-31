import numpy as np

from setup import *

def mutate_meme(meme):
    for i in range(str_len):
        if np.random.random() < cult_mut_rate:
            meme[i] = 1 - meme[i]

    return meme

def hamming_fitness(guess, goal):
    diff = np.logical_xor(guess, goal)
    dist = sum(diff) / (str_len)
    return (1 - dist)

def to_str(list):
    return ''.join([str(e) for e in list])
