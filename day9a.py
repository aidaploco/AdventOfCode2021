import numpy as np


def low_points_recursively(heightmap, i, j, low_points):
    if low_points[i][j] != 9:
        #print("1: ", low_points[i][j], i, j)
        return low_points[i][j]
    if heightmap[i][j] < heightmap[i-1][j] and heightmap[i][j] < heightmap[i+1][j] and \
                          heightmap[i][j] < heightmap[i][j-1] and \
                          heightmap[i][j] < heightmap[i][j+1]:
        #print("2: ", heightmap[i][j], i, j)
        return heightmap[i][j]
        
    if heightmap[i][j] > heightmap[i][j-1]:
        #print("3: ", low_points[i][j-1])
        low_points[i][j-1] = low_points_recursively(heightmap, i, j-1, low_points)
        #print("4: ", low_points[i][j-1])
    if heightmap[i][j] > heightmap[i][j+1]:
        #print("3: ", low_points[i][j+1])
        low_points[i][j+1] = low_points_recursively(heightmap, i, j+1, low_points)
        #print("4: ", low_points[i][j+1])
    if heightmap[i][j] > heightmap[i-1][j]:
        #print("3: ", low_points[i-1][j])
        low_points[i-1][j] = low_points_recursively(heightmap, i-1, j, low_points)
        #print("4: ", low_points[i-1][j])
    if heightmap[i][j] > heightmap[i+1][j]:
        #print("3: ", low_points[i+1][j])
        low_points[i+1][j] = low_points_recursively(heightmap, i+1, j, low_points)
        #print("4: ", low_points[i+1][j])
    
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
    
    low_points += 1
    risk_sum = sum(low_points[np.where(low_points != 10)])
    return risk_sum          


if __name__ == "__main__":
    f = open('day9').read().strip().split('\n')
    f = np.array(f)

    heightmap = []
    for i, nr in enumerate(f):
        heightmap.append(np.array([int(char) for char in nr]))
    heightmap = np.array(heightmap)
    print(len(heightmap), len(heightmap[0]))

    heightmap = np.pad(heightmap, 1, mode='maximum')
    print(heightmap)

    print(low_points(heightmap))