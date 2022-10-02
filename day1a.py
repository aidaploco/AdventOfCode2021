import pathlib


def greater_than(list_):
    counter = 0
    for i in range(len(list_) - 1):
        if list_[i+1] > list_[i]:
            counter += 1

    return counter


if __name__ == "__main__":
    #list_ = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    list_ = []

    filename = f"{pathlib.Path().resolve()}/day1"

    with open(filename) as file:
        while (line := file.readline().rstrip()):
            list_.append(int(line))

    print(greater_than(list_))
