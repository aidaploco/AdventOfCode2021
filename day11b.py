import numpy as np


def flash_recursively(octopuses, i, j, flashed, counter, step):
    print(len(np.where(octopuses == 0)[0]), step)
    if octopuses[i][j] == -1:
        return counter
    if flashed[i][j] != 0:
        return counter
    if 0 < octopuses[i][j] < 9:
        octopuses[i][j] += 1
        return counter
    
    flashed[i][j] = 1
    counter += 1
    octopuses[i][j] = 0
    counter = flash_recursively(octopuses, i, j+1, flashed, counter, step)
    counter = flash_recursively(octopuses, i, j-1, flashed, counter, step)
    counter = flash_recursively(octopuses, i+1, j, flashed, counter, step)
    counter = flash_recursively(octopuses, i-1, j, flashed, counter, step)
    counter = flash_recursively(octopuses, i-1, j+1, flashed, counter, step)
    counter = flash_recursively(octopuses, i+1, j+1, flashed, counter, step)
    counter = flash_recursively(octopuses, i-1, j-1, flashed, counter, step)
    counter = flash_recursively(octopuses, i+1, j-1, flashed, counter, step)

    return counter


def dumbo_octopus(octopuses):
    flashed = np.full([12, 12], 0)
    counter = 0
    for step in range(350):
        octopuses[np.where(octopuses != -1)] += 1
        octopuses[np.where(octopuses > 9)] = 0
        if len(np.where(octopuses == 0)[0]) > 0:
            for i, j in zip(np.where(octopuses == 0)[0], np.where(octopuses == 0)[1]):
                counter = flash_recursively(octopuses, i, j, flashed, counter, step)
                
        flashed = np.full([12, 12], 0)

    return counter


if __name__ == "__main__":
    f = open('day11').read().strip().split('\n')
    f = np.array(f)

    octopuses = []
    for octopussies in f:
        octopuses.append(np.array([int(octo) for octo in octopussies]))
    octopuses = np.array(octopuses)
    octopuses = np.pad(octopuses, 1, mode='constant', constant_values=-1)
    
    print(dumbo_octopus(octopuses))
    