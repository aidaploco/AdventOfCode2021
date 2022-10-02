import statistics
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
    horizontal_positions = defaultdict()

    for i in range(most_common_position, mean_position + 1):
        horizontal_positions[i] = abs(crabs - i)

    sum_horizontal_positions = [sum(v) for k,v in horizontal_positions.items()]
    return min(sum_horizontal_positions)  


if __name__ == "__main__":
    f = open('day7').read().strip()
    crabs = [int(number) for number in f.split(',')]
    print(count_fuel(crabs))
    
