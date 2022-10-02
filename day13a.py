import numpy as np
from contextlib import redirect_stdout


def fold_paper(paper, coordinates, fold):
    if fold[0] == 'x':
        right_half = [(y, x) for x, y in coordinates if x > paper.shape[1] / 2]
        for x, y in right_half:
            new_y = paper.shape[1] - y - 1
            paper[x][new_y] = '#'
        paper = paper[:,:int(paper.shape[1] / 2)]
    if fold[0] == 'y':
        lower_half = [(y, x) for x, y in coordinates if y > paper.shape[0] / 2]
        for x, y in lower_half:
            new_x = paper.shape[0] - x - 1
            paper[new_x][y] = '#'
        paper = paper[:int(paper.shape[0] / 2),:]

    return paper    


if __name__ == "__main__":
    f = open('day13').read().strip().split('\n')
    coordinates = f[:f.index('')]
    coordinates = [int(i) for x in coordinates for i in x.split(',')]
    coordinates = [(coordinates[i], coordinates[i+1]) for i in range(0, len(coordinates) - 1, 2)]
    
    max_x, max_y = 0, 0
    for x, y in coordinates:
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
    
    folds = f[f.index('') + 1:]
    folds = [f.strip('foldang ') for f in folds]

    paper = np.chararray((max_y + 1, max_x + 1))
    print(paper.shape[0], paper.shape[1])
    paper[:] = '.'
    for x, y in coordinates:
        paper[y][x] = '#'

    for fold in folds:
        paper = fold_paper(paper, coordinates, fold)
        coordinates = np.where(paper.find(b'#') == 0)
        coordinates = [(y, x) for x, y in zip(coordinates[0], coordinates[1])]

    #print(paper)
    
    with open('day13b.txt', 'w') as f:
        with redirect_stdout(f):
            print(paper)
