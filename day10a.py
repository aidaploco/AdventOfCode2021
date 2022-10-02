import numpy as np
from collections import deque


def corrupt_character(l):
    i = 0
    indices = {')': 99999, ']': 99999, '}': 99999, '>': 99999}
    while i < len(l):
        for x in [')', ']', '}', '>']:
            try:
                index = l.index(x)
                if index is not None:
                    indices[x] = index
            except:
                pass
        i += 1
    min_index = 99999
    min_key = ''
    for k, v in indices.items():
        if min_index > v:
            min_index = v
            min_key = k

    return min_key
        


def navigation_subsystem(f):
    corrupt_characters = []
    for x, line in enumerate(f):
        i = 0
        l = deque()
        while(i < len(line)):            
            l.append(line[i])
            if (line[i-1] == '(' and line[i] == ')') or (line[i-1] == '[' and line[i] == ']') \
                or (line[i-1] == '{' and line[i] == '}') or (line[i-1] == '<' and line[i] == '>'):
                l.pop()
                l.pop()
                del line[i]
                del line[i-1]
                i = len(l) - 1
            i += 1   
        corrupt_characters.append(corrupt_character(l))

    corrupt_characters = np.array(corrupt_characters)
    return corrupt_characters[np.where((corrupt_characters != None) & (corrupt_characters != ''))]


def syntax_checker(corrupt_characters):
    error_score = {')': 3, ']': 57, '}': 1197, '>': 25137}
    syntax_error_score = 0
    for cc in corrupt_characters:
        syntax_error_score += error_score[cc]
    
    return syntax_error_score


if __name__ == "__main__":
    f = open('day10').read().strip().split('\n')
    f = [deque(l) for l in f]
    
    corrupt_characters = navigation_subsystem(f)
    print(syntax_checker(corrupt_characters))