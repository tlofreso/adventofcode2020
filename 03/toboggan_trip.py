from rich import print
import math


def values():
    """Reads input, and returns each line as a list"""

    with open("input.txt") as f:
        my_input = f.read().splitlines()

    return my_input


def xmas_vacation():

    forest_map = values()
    right_int = 7
    down_int = 1
    shift = right_int
    trees = []

    for right, down in zip(forest_map, forest_map[down_int:]):
        down = down * 100
        spot = down[shift]
        shift += right_int
        trees.append(spot)

    return trees


def xmas_vacation2():

    forest_map = values()
    right_ints = [1, 3, 5, 7, 1]
    down_ints = [1, 1, 1, 1, 2]
    all_runs = []

    for right_int, down_int in zip(right_ints, down_ints):
        trees = []
        shift = right_int
        if down_int == 1:
            for right, down in zip(forest_map, forest_map[down_int:]):
                down = down * 500
                spot = down[shift]
                shift += right_int
                trees.append(spot)
        else:
            for right, down in zip(forest_map, forest_map[down_int::down_int]):
                down = down * 500
                spot = down[shift]
                shift += right_int
                trees.append(spot)
        all_runs.append(trees.count("#"))

    return all_runs


if __name__ == "__main__":

    answer1 = xmas_vacation()
    print(answer1.count("#"))
    answer2 = xmas_vacation2()
    print(math.prod(answer2))
