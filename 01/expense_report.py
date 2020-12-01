

def values():
    """Reads input, and returns all values as a sorted list of integers"""

    with open('input.txt') as f:
        lines = f.read().splitlines()
        my_input = [int(i) for i in lines]
        my_input.sort()

    return my_input


def computer():

    result = 2020

    n1_possible = []
    n2_possible = []

    # Get possible first and second operators
    for num in values():
        if num <= result / 2:
            n1_possible.append(num)
        else:
            n2_possible.append(num)

    # Crunch result
    for n1 in n1_possible:
        for n2 in n2_possible:
            if n1 + n2 == result:
                solution1 = n1 * n2

    return solution1, n1_possible, n2_possible


def computer2():

    result = 2020

    n1_n2 = computer()[1]
    n3 = computer()[2]

    possible = []

    for n1 in n1_n2:
        for n2 in n1_n2:
            if n1 + n2 <= result / 2:
                possible_operators = [n1, n2]
                possible.append(possible_operators)

    for n1 in possible:
        for n2 in n3:
            if sum(n1) + n2 == result:
                solution2 = n1[0] * n1[1] * n2

    return solution2


if __name__ == "__main__":

    answer1 = computer()[0]
    print(answer1)

    answer2 = computer2()
    print(answer2)
