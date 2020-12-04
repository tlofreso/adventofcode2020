"""
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
"""

from rich import print
import os, re


def values():

    with open("input.txt") as f:
        my_input = f.read().split(2 * os.linesep)

    return my_input


def regexer():

    data = values()

    matcher = re.compile(r"(?P<birth_year>byr:\d\d\d\d)")
    test = matcher.match(data[0])
    print(test)

    print(data[0])
    for line in data[0].splitlines():
        m = matcher.match(line)
        # m = re.match(r"(?P<birth_year>byr:\d\d\d\d)", line)
        print(m)
        # print(m.group("birth_year"))


if __name__ == "__main__":
    regexer()
