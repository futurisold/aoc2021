from typing import NamedTuple, Iterator
from collections import Counter


class Point(NamedTuple):
    x: int
    y: int

    @staticmethod
    def parse(raw: str) -> 'Point':
        x, y = raw.split(',')
        return Point(int(x), int(y))


class Line(NamedTuple):
    start: Point
    end: Point

    def is_horizontal(self) -> bool:
        return self.start.y == self.end.y

    def is_vertical(self) -> bool:
        return self.start.x == self.end.x

    def points_on_line(self) -> Iterator[Point]:
        if self.is_horizontal():
            lo = min(self.start.x, self.end.x)
            hi = max(self.start.x, self.end.x)

            for x in range(lo, hi+1):
                yield Point(x, self.start.y)

        elif self.is_vertical():
            lo = min(self.start.y, self.end.y)
            hi = max(self.start.y, self.end.y)

            for y in range(lo, hi+1):
                yield Point(self.start.x, y)
        else:
            x_lo = min(self.start.x, self.end.x)
            x_hi = max(self.start.x, self.end.x)

            dx = self.end.x - self.start.x
            dy = self.end.y - self.start.y
            slope_up = dx * dy > 0

            x = x_lo
            y = self.start.y if x_lo == self.start.x else self.end.y

            for i in range(x_hi - x_lo + 1):
                yield Point(x, y)
                x += 1
                y += (1 if slope_up else -1)

    @staticmethod
    def parse(raw: str) -> 'Line':
        start_line, end_line = raw.split(' -> ')
        return Line(Point.parse(start_line), Point.parse(end_line))


def count_vents(lines: Iterator[Line], hv_only=True) -> int:
    counts = Counter(
        point
        for line in lines
        if any([not hv_only, line.is_horizontal(), line.is_vertical()])
        for point in line.points_on_line()
    )
    return sum(count > 1 for count in counts.values())


with open('assert.txt') as f:
    raw = f.read().splitlines()
    lines = [Line.parse(line) for line in raw]


assert count_vents(lines) == 5
assert count_vents(lines, hv_only=False) == 12


if __name__ == '__main__':
    with open('input.txt') as f:
        raw = f.read().splitlines()
        lines = [Line.parse(line) for line in raw]
    print(count_vents(lines))
    print(count_vents(lines, hv_only=False))

