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
    good_passports = []

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
                good_passports.append(passport)

    return good_passports


def puzzle2():

    passports = puzzle1()

    # Check birth year
    # print(len(passports))
    for passport in passports:
        for e in passport:
            if e.startswith("byr"):
                if int(e[4:]) < 1920 or int(e[4:]) > 2002:
                    passports.remove(passport)

    # Check issue year
    # print(len(passports))
    for passport in passports:
        for e in passport:
            if e.startswith("iyr"):
                if int(e[4:]) < 2010 or int(e[4:]) > 2020:
                    passports.remove(passport)

    # Check expire year
    # print(len(passports))
    for passport in passports:
        for e in passport:
            if e.startswith("eyr"):
                if int(e[4:]) < 2020 or int(e[4:]) > 2030:
                    passports.remove(passport)

    # Check height in cm
    # print(len(passports))
    for passport in passports:
        for e in passport:
            if e.startswith("hgt"):
                if e.endswith("cm"):
                    h_cm = re.findall(r"\d+", e)
                    if int(h_cm[0]) < 150 or int(h_cm[0]) > 193:
                        passports.remove(passport)

    # Check height in in
    # print(len(passports))
    for passport in passports:
        for e in passport:
            if e.startswith("hgt"):
                if e.endswith("in"):
                    h_in = re.findall(r"\d+", e)
                    if int(h_in[0]) < 59 or int(h_in[0]) > 76:
                        passports.remove(passport)

    # Check for invalid height
    # print(len(passports))
    for passport in passports:
        for e in passport:
            if e.startswith("hgt"):
                if not re.match(r"hgt:\d*(cm|in)", e):
                    passports.remove(passport)

    # Check hair color
    # print(len(passports))
    for passport in passports:
        for e in passport:
            if e.startswith("hcl"):
                if not re.match(r"hcl\:\#[a-f,0-9]{6}", e):
                    passports.remove(passport)

    # Check eye color
    # print(len(passports))
    required = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
    for passport in passports:
        for e in passport:
            if e.startswith("ecl"):
                if not re.match(
                    r"ecl:amb|ecl:blu|ecl:brn|ecl:gry|ecl:grn|ecl:hzl|ecl:oth", e
                ):
                    passports.remove(passport)

    # Check passport ID
    # print(len(passports))
    for passport in passports:
        for e in passport:
            if e.startswith("pid"):
                if not re.match(r"pid:[0-9]{9}", e):
                    passports.remove(passport)

    for passport in passports:
        for e in passport:
            if e.startswith("pid"):
                if len(e) > 13:
                    passports.remove(passport)

    return passports


if __name__ == "__main__":

    print(len(puzzle1()))
    print(len(puzzle2()))