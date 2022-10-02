import pathlib
import copy
from collections import defaultdict


def determine_oxygen_rating(oxygen_positions):
    for k, v in oxygen_positions.items():
        if len(v) <= 1:
            break
            
        if (sum(v) / len(v)) >= 0.5:
            indices = [i for i, x in enumerate(oxygen_positions[k]) if x == 0]
            for k in oxygen_positions.keys():
                for i in sorted(indices, reverse=True):
                    del oxygen_positions[k][i]
        else:
            indices = [i for i, x in enumerate(oxygen_positions[k]) if x == 1]
            for k in oxygen_positions.keys():
                for i in sorted(indices, reverse=True):
                    del oxygen_positions[k][i]

    oxygen = ""
    for k in oxygen_positions.keys():
        oxygen += oxygen.join(str(oxygen_positions[k][0]))

    return int(oxygen, 2)


def determine_co2_rating(co2_positions):
    for k, v in co2_positions.items():
        if len(v) <= 1:
            break

        if (sum(v) / len(v)) >= 0.5:
            indices = [i for i, x in enumerate(co2_positions[k]) if x == 1]
            for k in co2_positions.keys():
                for i in sorted(indices, reverse=True):
                    del co2_positions[k][i]
        else:
            indices = [i for i, x in enumerate(co2_positions[k]) if x == 0]
            for k in co2_positions.keys():
                for i in sorted(indices, reverse=True):
                    del co2_positions[k][i]

    co2 = ""
    for k in co2_positions.keys():
        co2 += co2.join(str(co2_positions[k][0]))

    return int(co2, 2)


if __name__ == "__main__":
    positions = []
    corresponding_positions = defaultdict(list)
    filename = f"{pathlib.Path().resolve()}/day3"

    with open(filename) as file:
        while (line := file.readline().rstrip()):
            positions.append(line)    

    for j in range(len(positions[0])):
        for i in range(len(positions)):
            corresponding_positions[j].append(int(positions[i][j]))

    oxygen_positions = copy.deepcopy(corresponding_positions)
    co2_positions = copy.deepcopy(corresponding_positions)

    oxygen = determine_oxygen_rating(oxygen_positions)
    co2 = determine_co2_rating(co2_positions)

    print(oxygen * co2)
    