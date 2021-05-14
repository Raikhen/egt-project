import random
import numpy as np

# Parameters
poly_deg = 5
poly_min = -2
poly_max = 2

def random_polynomial():
    return np.random.uniform(
        low = poly_min,
        high = poly_max,
        size = (poly_deg + 1, poly_deg + 1)
    )

def get_copying(polynomial):
    def copying(x, y):
        s = 0

        for i, p in enumerate(polynomial):
            for j, c in enumerate(p):
                s += c * pow(x, i) * pow(y, j)

        return np.clip(s, 0, 1)

    return copying
