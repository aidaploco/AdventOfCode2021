import pathlib
from collections import defaultdict


def life_support_rating(corresponding_positions):    
    most_common_bit, least_common_bit = [], []   

    for k, v in corresponding_positions.items():
        if (sum(v) / len(v)) >= 0.5:
            most_common_bit.append(str(1))
            least_common_bit.append(str(0))
        else:
            most_common_bit.append(str(0))
            least_common_bit.append(str(1))

    gamma_rate = "".join(most_common_bit)
    epsilon_rate = "".join(least_common_bit)

    return int(gamma_rate, 2) * int(epsilon_rate, 2)


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

    print(life_support_rating(corresponding_positions))
    