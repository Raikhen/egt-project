import random

def random_polynomial():
    # This implementation is incorrect
    
    polynomial = []

    for _ in range(3):
        p = []

        for _ in range(poly_deg + 1):
            p.append(random.uniform(poly_min, poly_max))

        polynomial.append(p)

    return polynomial

def normalize(polynomial):
