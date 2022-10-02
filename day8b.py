def assign_score(a=8, b=6, c=8, d=7, e=4, f=9, g=7):
    zero = a + b + c + e + f + g
    one = c + f
    two = a + c + d + e + g
    three = a + c + d + f + g
    four = b + c + d + f
    five = a + b + d + f + g
    six = a + b + d + e + f + g
    seven = a + c + f
    eight = a + b + c + d + e + f + g
    nine = a + b + c + d + f + g

    digits = [zero, one, two, three, four, five, six, seven, eight, nine]
    return digits


def decode_input(segments_input):
    char_counts = []
    for line in segments_input:
        char_count = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0}
        for s in line:
            if s == ' ':
                continue
            char_count[s] += 1
        char_counts.append(char_count)
        
    return char_counts


def decode_output(segments_output, char_counts):
    digit_scores = assign_score()
    digits = []

    for nr, line in enumerate(segments_output):
        char_sum = [0, 0, 0, 0]
        digits_row = ''
        counter = 0
        for s in line:
            if s == ' ':
                counter += 1
                continue
            char_sum[counter] += char_counts[nr][s]

        counter = 0
        for cs in char_sum:
            for i, ds in enumerate(digit_scores):
                if cs == ds:
                    digits_row += str(i)
                    counter += 1   
        digits.append(int(digits_row))    

    digits = sum(digits)
    return digits


if __name__ == "__main__":
    f = open('day8').read().strip().split('\n')
    segments_input = [x.split(' | ')[0] for x in f]
    segments_output = [x.split(' | ')[1] for x in f]
    
    char_counts = decode_input(segments_input)
    print(decode_output(segments_output, char_counts))

