import statistics
import math
import numpy as np
from collections import defaultdict


def get_statistics(crabs):
    crabs_sorted = sorted(crabs)
    most_common_position = max(crabs, key=crabs.count)
    median_position = statistics.median(crabs_sorted)
    mean_position = statistics.mean(crabs)

    return most_common_position, median_position, round(mean_position)


def count_fuel(crabs):
    most_common_position, median_position, mean_position = get_statistics(crabs)
    crabs = np.array(crabs)
    counter = 0
    horizontal_positions = defaultdict(list)

    for i in range(most_common_position, mean_position + 1):   
        for c in crabs:
            if c > i:
                horizontal_positions[i].append(sum(range(c - i + 1)))
            else:
                horizontal_positions[i].append(sum(range(i - c + 1)))

    sum_horizontal_positions = [sum(v) for k,v in horizontal_positions.items()]
    return min(sum_horizontal_positions)  


if __name__ == "__main__":
    f = open('day7').read().strip()
    crabs = [int(number) for number in f.split(',')]
    print(count_fuel(crabs))
    