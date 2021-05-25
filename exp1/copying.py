import random
import numpy as np
from scipy.optimize import minimize

# Parameters
poly_deg = 1
poly_min = -2
poly_max = 2
mut_rate = .05

def random_polynomial():
    return np.random.uniform(
        low = poly_min,
        high = poly_max,
        size = (poly_deg + 1, poly_deg + 1)
    )

def normalize(f):
    g = lambda x: f(x[0], x[1])
    h = lambda x: -f(x[0], x[1])

    min_pos = minimize(g, x0 = (0.5, 0.5), bounds=((0, 1), (0, 1))).x
    max_pos = minimize(h, x0 = (0.5, 0.5), bounds=((0, 1), (0, 1))).x

    minv = g(min_pos)
    maxv = g(max_pos)

    def normalized(x, y):
        return (f(x, y) - minv) / (maxv - minv)

    return normalized

def get_copying(polynomial):
    def copying(x, y):
        s = 0

        for i, p in enumerate(polynomial):
            for j, c in enumerate(p):
                s += c * pow(x, i) * pow(y, j)

        return s

    return normalize(copying)

def mutate(polynomial):
    s = np.random.normal(0, mut_rate, size = (poly_deg + 1, poly_deg + 1))
    return s + polynomial
