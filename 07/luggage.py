from rich import print


def values():

    with open("input.txt") as f:
        my_input = f.read().splitlines()

    return my_input


if __name__ == "__main__":

    print(values())