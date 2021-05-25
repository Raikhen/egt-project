import random
import numpy as np

from utils import normalize

# Parameters
poly_deg = 1
poly_min = -2
poly_max = 2
mut_rate = .05

class DNA:
    def __init__(self, parent = -1):
        if parent == -1:
            self.polynomial = np.random.uniform(
                low = poly_min,
                high = poly_max,
                size = (poly_deg + 1, poly_deg + 1)
            )
        else:
            s = np.random.normal(0, mut_rate, size=(poly_deg + 1, poly_deg + 1))
            self.polynomial = s + parent.polynomial

    def get_copying(self, normalized = True):
        def copying(x = 1, y = 1, as_text = False):
            s = 0
            text = ''

            for i, p in enumerate(self.polynomial):
                for j, c in enumerate(p):
                    s += c * pow(x, i) * pow(y, j)
                    text += f'{round(c, 2)}(x^{i})(y^{j}) +'

            return text[:-2] if as_text else s

        return normalize(copying) if normalized else copying

    def __repr__(self):
        f = self.get_copying(normalized = False)
        return f(as_text = True)
