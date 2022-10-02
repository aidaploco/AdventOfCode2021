import numpy as np
from functools import reduce


def low_points_recursively(heightmap, i, j, low_points):
    if low_points[i][j] != 9:
        return low_points[i][j]
    if heightmap[i][j] < heightmap[i-1][j] and heightmap[i][j] < heightmap[i+1][j] and \
                          heightmap[i][j] < heightmap[i][j-1] and \
                          heightmap[i][j] < heightmap[i][j+1]:
        return heightmap[i][j]
        
    if heightmap[i][j] > heightmap[i][j-1]:
        low_points[i][j-1] = low_points_recursively(heightmap, i, j-1, low_points)
    if heightmap[i][j] > heightmap[i][j+1]:
        low_points[i][j+1] = low_points_recursively(heightmap, i, j+1, low_points)
    if heightmap[i][j] > heightmap[i-1][j]:
        low_points[i-1][j] = low_points_recursively(heightmap, i-1, j, low_points)
    if heightmap[i][j] > heightmap[i+1][j]:
        low_points[i+1][j] = low_points_recursively(heightmap, i+1, j, low_points)
    
    return 9


def low_points(heightmap):
    i, j = 1, 1
    length, width = len(heightmap), len(heightmap[0])
    low_points = np.full([length, width], 9)
    while(i < length - 1):
        while(j < width - 1):
            low_points_recursively(heightmap, i, j, low_points)
            j += 1
        j = 1
        i += 1
    
    return low_points        


def find_basins_recursively(heightmap, i, j, visited, counter):
    if heightmap[i][j] == 9:
        return counter
    if visited[i][j] != 0:
        return counter
    
    visited[i][j] = 1
    counter += 1
    counter = find_basins_recursively(heightmap, i, j-1, visited, counter)
    counter = find_basins_recursively(heightmap, i, j+1, visited, counter)
    counter = find_basins_recursively(heightmap, i-1, j, visited, counter)
    counter = find_basins_recursively(heightmap, i+1, j, visited, counter)

    return counter


def find_basins(heightmap, low_points):
    i, j = 1, 1
    length, width = len(heightmap), len(heightmap[0])
    visited = np.full([length, width], 0)
    basins = []
    counter = 0
    while(i < length - 1):
        while(j < width - 1):
            if low_points[i][j] != 9:
                basins.append(find_basins_recursively(heightmap, i, j, visited, counter))
                counter = 0
            j += 1
        j = 1
        i += 1
    
    three_biggest_basins = sorted(basins, reverse=True)[:3]
    return reduce(lambda x, y: x * y, three_biggest_basins)    


if __name__ == "__main__":
    f = open('day9').read().strip().split('\n')
    f = np.array(f)

    heightmap = []
    for i, nr in enumerate(f):
        heightmap.append(np.array([int(char) for char in nr]))
    heightmap = np.array(heightmap)
    heightmap = np.pad(heightmap, 1, mode='maximum')

    low_points = low_points(heightmap)
    print(find_basins(heightmap, low_points))