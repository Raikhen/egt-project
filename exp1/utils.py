from scipy.optimize import minimize

# Normalizes output to be between 0 and 1
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
