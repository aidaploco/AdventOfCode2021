import numpy as np


def winning_card(drawn_numbers, boards):
    while(True):
        drawn_number = drawn_numbers.pop(0)
        for i, b in enumerate(boards):
            location = np.where(b == drawn_number)
            if len(location[0]) > 0:
                boards[i][location[0][0]][location[1][0]] = -1
            
        for b in boards:
            for i in range(5):
                if np.all(b[i] == -1) or np.all(np.transpose(b)[i] == -1):
                    return b, drawn_number


def bingo(winning_card, drawn_number):
    score = sum(winning_card[np.where(winning_card != -1)])
    return score * drawn_number


if __name__ == "__main__":
    f = list(filter(None, open('day4').read().strip().split('\n')))

    drawn_numbers = f.pop(0)
    drawn_numbers = [int(number) for number in drawn_numbers.split(',')]

    f = [int(number) for s in f for number in s.split()]
    lines = []
    boards = []

    for i in range(0,len(f),5):
        lines.append(np.array(f[i:i+5]))

    for i in range(0,len(lines),5):
        boards.append(np.array(lines[i:i+5]))   

    winning_card, drawn_number = winning_card(drawn_numbers, boards)
    print(bingo(winning_card, drawn_number))



    