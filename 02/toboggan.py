from rich import print


def values():
    """Reads input, and returns each line as a list"""

    with open('input.txt') as f:
        lines = f.read().splitlines()
        my_input = [i.split() for i in lines]

    return my_input


def pwdValidator():

    password = values()

    valid = []
    invalid = []

    for e in password:
        policy_num = e[0].split('-')
        policy_key = e[1].strip(':')
        password = e[2]

        if password.count(policy_key) >= int(policy_num[0]):
            if password.count(policy_key) <= int(policy_num[1]):
                valid.append(password)
        else:
            invalid.append(password)

    return valid, invalid


def pwdValidator2():

    password = values()

    valid = []
    invalid = []

    for e in password:
        policy_num = e[0].split('-')
        policy_key = e[1].strip(':')
        password = e[2]

        if (password[int(policy_num[1]) - 1] == policy_key) and (password[int(policy_num[0]) - 1] == policy_key):
            invalid.append(password)

        if (password[int(policy_num[1]) - 1] != policy_key) and (password[int(policy_num[0]) - 1] != policy_key):
            invalid.append(password)

        if (password[int(policy_num[1]) - 1] != policy_key) and (password[int(policy_num[0]) - 1] == policy_key):
            valid.append(password)

        if (password[int(policy_num[1]) - 1] == policy_key) and (password[int(policy_num[0]) - 1] != policy_key):
            valid.append(password)

    return valid, invalid


if __name__ == "__main__":

    answer1 = pwdValidator()[0]
    print(len(answer1))

    answer2 = pwdValidator2()[0]
    print(len(answer2))
