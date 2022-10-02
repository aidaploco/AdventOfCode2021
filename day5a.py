import numpy as np


def hydrothermal_vents(grid, start, end):
    for c1, c2 in zip(start, end):
        x1, y1 = c1[0], c1[1]
        x2, y2 = c2[0], c2[1]
        if x1 > x2:
            distance = x1 - x2 + 1
            for i in range(distance):
                grid[y2][x2 + i] += 1
        elif x2 > x1:
            distance = x2 - x1 + 1
            for i in range(distance):
                grid[y1][x1 + i] += 1
        elif y1 > y2:
            distance = y1 - y2 + 1
            for i in range(distance):
                grid[y2 + i][x2] += 1
        elif y2 > y1:
            distance = y2 - y1 + 1
            for i in range(distance):
                grid[y1 + i][x1] += 1

    return grid


def create_grid(start, end):
    max_start = max(start)
    max_end = max(end)
    max_numbers = max(max(max_start, max_end))

    grid_size = max_numbers
    grid_size += 1
    grid = np.zeros((grid_size, grid_size))

    return grid


def filter_lines(f):
    start = [line.split(' -> ')[0] for line in f]
    end = [line.split(' -> ')[1] for line in f]
    start = [(int(coordinate.split(',')[0]), int(coordinate.split(',')[1])) for coordinate in start]
    end = [(int(coordinate.split(',')[0]), int(coordinate.split(',')[1])) for coordinate in end]
    start_filtered, end_filtered = [], []

    # Remove all lines that don't have the same x or y coordinate
    for c in zip(start, end):
        x1, y1 = c[0][0], c[0][1]
        x2, y2 = c[1][0], c[1][1]
        if x1 == x2 or y1 == y2:
            start_filtered.append((x1, y1))
            end_filtered.append((x2, y2))

    return start_filtered, end_filtered


if __name__ == "__main__":
    f = open('day5').read().strip().split('\n')
    start, end = filter_lines(f)    
    
    grid = create_grid(start, end)
    grid = hydrothermal_vents(grid, start, end)
    print(grid)
    print(len(np.where(grid > 1)[0]))
