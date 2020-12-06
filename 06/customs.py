import os
from rich import print


def values():

    with open("input.txt") as f:
        my_input = f.read().split(2 * os.linesep)
        my_input = list(map(lambda x: x.replace("\n", ""), my_input))

    return my_input


def puzzle1():

    yeses = []
    for group in values():
        yes = len(set(group))
        yeses.append(yes)

    return yeses


if __name__ == "__main__":
    print(sum(puzzle1()))
