from statistics import median
from typing import List


raw = open('assert.txt').read().strip()
positions = [int(x) for x in raw.split(',')]


def cost(n: int) -> int:
    # 1 + 2 + 3 ... + n = n(n+1)/2
    return n * (n+1) // 2


def least_fuel(positions: List[int], cst_rate: bool) -> int:
    if cst_rate:
        bp = int(median(positions))
        return sum(abs(p - bp) for p in positions)

    lo = min(positions)
    hi = max(positions)
    bp = min(range(lo, hi+1), key=lambda x: sum(cost(abs(p - x)) for p in positions))
    return sum(cost(abs(p - bp)) for p in positions)


assert least_fuel(positions, True) == 37
assert least_fuel(positions, False) == 168


if __name__ == '__main__':
    raw = open('input.txt').read().strip()
    positions = [int(x) for x in raw.split(',')]
    print(least_fuel(positions, True))
    print(least_fuel(positions, False))
