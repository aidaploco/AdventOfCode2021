import pathlib


def three_measurements(list_):
    counter = 0

    for i in range(2, len(list_) - 1):
        sum1 = list_[i] + list_[i-1] + list_[i-2]
        sum2 = list_[i] + list_[i-1] + list_[i+1]
        if sum2 > sum1:
            counter += 1

    return counter


if __name__ == "__main__":
    list_ = []
    filename = f"{pathlib.Path().resolve()}/day1"

    with open(filename) as file:
        while (line := file.readline().rstrip()):
            list_.append(int(line))

    print(three_measurements(list_))
