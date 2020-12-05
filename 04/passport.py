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
        puzzle_input = list(map(lambda x: x.replace("\n", " "), my_input))

    return puzzle_input


def regexer():

    # byr = re.compile(r"(?P<birth_year>byr:\d{4})")
    # iyr = re.compile(r"(?P<issue_year>iyr:\d{4})")
    # eyr = re.compile(r"(?P<expiration_year>eyr:\d{4})")
    # hgt = re.compile(r"(?P<height>hgt\:\d+\w+)")
    # hcl = re.compile(r"(?P<hair_color>hcl\:\S+)")
    # ecl = re.compile(r"(?P<eye_color>ecl\:\S+)")
    # pid = re.compile(r"(?P<passport_id>pid\:\S+)")
    # cid = re.compile(r"(?P<country_id>cid\:\S+)")

    r = re.compile(
        r"byr:\d{4}|iyr:\d{4}|eyr:\d{4}|hgt\:\d+\w+|hcl\:\S+|ecl\:\S+|pid\:\S+|cid\:\S+"
    )

    data = values()

    passports = []

    for e in data:
        parsed = r.findall(e)
        passports.append(parsed)

    return passports


def puzzle1():

    required = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
    passports = regexer()

    counter = 0

    for passport in passports:
        for e in passport:
            if e.startswith("cid"):
                passport.remove(e)

    for passport in passports:
        valid = []
        for e in passport:
            entry = e.startswith(required)
            valid.append(entry)

        if False not in valid:
            if len(valid) == 7:
                counter += 1

    return counter


if __name__ == "__main__":
    print(puzzle1())


# if all([x.startswith(y) for y in required]):
#                 print(x)