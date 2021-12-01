from itertools import tee
from typing import Iterable


def sliding_window(iterable, n=2):
    iterables = tee(iterable, n)
    for j in range(1, n+1):
        for i in iterables[j:]:
            next(i, None)
    return zip(*iterables)


def count_increases(measurements: Iterable[int]) -> int:
    pairs = sliding_window(measurements)
    res = 0

    for m1, m2 in pairs:
        if m2 > m1:
            res += 1

    return res


def count_increases_by_window(measurements: Iterable[int], window):
    window_measurements = [sum(w) for w in sliding_window(measurements, window)]

    return count_increases(window_measurements)
