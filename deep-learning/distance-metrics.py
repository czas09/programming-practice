import numpy as np


def euclidean(x, y):
    return np.sqrt(np.sum((x - y) ** 2))


def manhattan(x, y):
    return np.sum(np.abs(x - y))


def chebyshev(x, y):
    return np.max(np.abs(x - y))


def minkowski(x, y, p):
    return np.sum(np.abs(x - y) ** p) ** (1 / p)


def hamming(x, y):
    return np.sum(x != y) / len(x)