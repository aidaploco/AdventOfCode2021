import pathlib


def position(directions):
    horizontal, aim, depth = 0, 0, 0

    for x in directions:
        d, v = x.split()
        if d == "forward":
            horizontal += int(v)
            depth += int(v) * aim
        if d == "down":
            aim += int(v)
        if d == "up":
            aim -= int(v)

    return horizontal * depth


if __name__ == "__main__":
    directions = []
    filename = f"{pathlib.Path().resolve()}/day2"

    with open(filename) as file:
        while (line := file.readline().rstrip()):
            directions.append(line)

    print(position(directions))