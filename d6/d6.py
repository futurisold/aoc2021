from typing import List


class LanternFish:
    def __init__(self, timers: List[int]) -> None:
        self.timers = [0 for i in range(9)]
        for timer in timers:
            self.timers[timer] += 1

    def step(self) -> None:
        new_timers = self.timers[1:] + [0]
        new_timers[8] += self.timers[0]
        new_timers[6] += self.timers[0]
        self.timers = new_timers

    def count(self) -> int:
        return sum(self.timers)


with open('assert.txt') as f:
    raw = f.read()
    timers = [int(x) for x in raw.split(',') if x]

lf = LanternFish(timers)
for _ in range(18):
    lf.step()
assert lf.count() == 26

for _ in range(256-18):
    lf.step()
assert lf.count() == 26984457539


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read()
        timers = [int(x) for x in raw.split(',') if x]
    lf = LanternFish(timers)
    for _ in range(80):
        lf.step()
    print(lf.count())
    for _ in range(256-80):
        lf.step()
    print(lf.count())

