import pathlib
from collections import defaultdict


def position(directions):
    horizontal = sum(directions['forward'])
    down = sum(directions['down'])
    up = sum(directions['up'])
    depth = down - up

    return horizontal * depth


if __name__ == "__main__":
    directions = defaultdict(list)
    filename = f"{pathlib.Path().resolve()}/day2"

    with open(filename) as file:
        while (line := file.readline().rstrip()):
            directions[line.split()[0]].append(int(line.split()[1]))

    print(position(directions))