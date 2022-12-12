import numpy as np


with open('assert.txt') as f:
    raw = f.read()
    diag_report = np.array([list(map(int, x)) for x in raw.split('\n') if x])


def power_consumption(diag_report):
    ones = np.count_nonzero(diag_report, axis=0)
    zeros = len(diag_report) - ones
    gamma_rate = int(''.join(map(lambda x: str(int(x)), ones > zeros)), 2)
    eps_rate   = int(''.join(map(lambda x: str(int(x)), zeros > ones)), 2)
    return gamma_rate * eps_rate


def o2_gen_rating(diag_report):
    buffer = diag_report.copy()
    bit = 0
    found = False
    while not found:
        digits = buffer[:, bit]
        ones = np.where(digits == 1)[0]
        zeros = np.where(digits == 0)[0]
        if len(ones) >= len(zeros):
            buffer = buffer[ones]
        else:
            buffer = buffer[zeros]
        bit += 1

        if len(buffer) == 1:
            found = True
    return int(''.join(map(lambda x: str(x), buffer[0])), 2)


def co2_gen_rating(diag_report):
    buffer = diag_report.copy()
    bit = 0
    found = False
    while not found:
        digits = buffer[:, bit]
        ones = np.where(digits == 1)[0]
        zeros = np.where(digits == 0)[0]
        if len(ones) >= len(zeros):
            buffer = buffer[zeros]
        else:
            buffer = buffer[ones]
        bit += 1

        if len(buffer) == 1:
            found = True
    return int(''.join(map(lambda x: str(x), buffer[0])), 2)


def life_support_rating(diag_report):
    o2 = o2_gen_rating(diag_report)
    co2 = co2_gen_rating(diag_report)
    return o2 * co2


assert power_consumption(diag_report) == 198
assert life_support_rating(diag_report) == 230


with open('input.txt') as f:
    raw = f.read()
    diag_report = np.array([list(map(int, x)) for x in raw.split('\n') if x])


print(power_consumption(diag_report))
print(life_support_rating(diag_report))


