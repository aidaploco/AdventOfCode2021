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
    incomplete_lines = []
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
        if corrupt_character(l) == '':
            incomplete_lines.append(x)

    return incomplete_lines


def autocomplete_checker(incomplete_lines):
    character_score = {'(': 1, '[': 2, '{': 3, '<': 4}
    total_scores = []
    for il in incomplete_lines:
        total_score = 0
        while len(il) > 0:
            total_score *= 5
            total_score += character_score[il.pop()]
        total_scores.append(total_score)
    
    total_scores = sorted(total_scores)
    middle_score = total_scores[round(len(total_scores) / 2) - 1]

    return middle_score


if __name__ == "__main__":
    f = open('day10').read().strip().split('\n')
    f = [deque(l) for l in f]
    
    incomplete_lines = navigation_subsystem(f)
    incomplete_lines = [l for i, l in enumerate(f) if i in incomplete_lines]
    print(autocomplete_checker(incomplete_lines))