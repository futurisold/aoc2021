with open('assert.txt') as f:
    raw = f.read()
    report = [int(x) for x in raw.split('\n') if x]


def compute_depth(report, w):
    depth = 0
    i, j = 0, 1
    while j < len(report):
        if sum(report[i:i+w]) < sum(report[j:j+w]):
            depth += 1
        i += 1
        j += 1
    return depth

assert compute_depth(report, 1) == 7
assert compute_depth(report, 3) == 5


with open('input.txt') as f:
    raw = f.read()
    report = [int(x) for x in raw.split('\n') if x]

print(compute_depth(report, 1))
print(compute_depth(report, 3))
