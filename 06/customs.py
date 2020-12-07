import os
from rich import print


def values():

    with open("input.txt") as f:
        my_input = f.read().split(2 * os.linesep)
        puzzle1_input = list(map(lambda x: x.replace("\n", ""), my_input))

    return puzzle1_input, my_input


def puzzle1():

    yeses = []
    for group in values()[0]:
        yes = len(set(group))
        yeses.append(yes)

    return yeses


def puzzle2():

    yeses = []
    for group in values()[1]:
        group = group.splitlines()
        yes = len(set(group[0]).intersection(*group))
        yeses.append(yes)

    return yeses


if __name__ == "__main__":

    print(sum(puzzle1()))
    print(sum(puzzle2()))
