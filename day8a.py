if __name__ == "__main__":
    f = open('day8').read().strip().split('\n')
    digit_output = [output.split(' | ')[1] for output in f]
    digits = []
    for do in digit_output:
        digits.extend(do.split())

    counter = 0
    for d in digits:
        if len(d) in [2,3,4,7]:
            counter += 1

    print(counter)