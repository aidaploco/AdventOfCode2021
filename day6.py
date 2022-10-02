import numpy as np
from collections import defaultdict


def simulate_fish(lantern_fish):
    for i in range(1, 257):
        lantern_fish[i] = lantern_fish[i-1] - 1
        lantern_fish[i][np.where(lantern_fish[i] == -1)] = 6

        new_fishes = len(np.where(lantern_fish[i-1] == 0)[0])
        for _ in range(new_fishes):
            lantern_fish[i] = np.append(lantern_fish[i], 8)

    last_key = sorted(lantern_fish.keys())[-1]

    return len(lantern_fish[last_key])



if __name__ == "__main__":
    lantern_fish = defaultdict()
    f = open('day6').read().strip()
    lantern_fish[0] = np.array([int(number) for number in f.split(',')])

    print(simulate_fish(lantern_fish))