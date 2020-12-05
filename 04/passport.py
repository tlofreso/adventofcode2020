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

    byr = re.compile(r"(?P<birth_year>byr:\d{4})")
    iyr = re.compile(r"(?P<issue_year>iyr:\d{4})")
    eyr = re.compile(r"(?P<expiration_year>eyr:\d{4})")
    hgt = re.compile(r"(?P<height>hgt\:\d+\w+)")
    hcl = re.compile(r"(?P<hair_color>hcl\:\S+)")
    ecl = re.compile(r"(?P<eye_color>ecl\:\S+)")
    pid = re.compile(r"(?P<passport_id>pid\:\S+)")
    cid = re.compile(r"(?P<country_id>cid\:\S+)")

    test = []
    for line in data:

        if byr.match(line) is not None:
            birth_yr = byr.match(line)
        else:
            birth_yr = None

        if iyr.match(line) is not None:
            issue_yr = iyr.match(line)
        else:
            issue_yr = None

        if eyr.match(line) is not None:
            expire_yr = eyr.match(line)
        else:
            expire_yr = None

        if hgt.match(line) is not None:
            height = hgt.match(line)
        else:
            height = None

        if hcl.match(line) is not None:
            hair_color = hcl.match(line)
        else:
            hair_color = None

        if ecl.match(line) is not None:
            eye_color = ecl.match(line)
        else:
            eye_color = None

        if pid.match(line) is not None:
            passport_id = pid.match(line)
        else:
            passport_id = None

        if cid.match(line) is not None:
            country_id = cid.match(line)
        else:
            country_id = None

        test.append(
            birth_yr.group("birth_year"),
            issue_yr.group("issue_year"),
            expire_yr.group("expiration_year"),
            height.group("height"),
            hair_color.group("hair_color"),
            eye_color.group("eye_color"),
            passport_id.group("passport_id"),
            country_id.group("country_id"),
        )

    return test


if __name__ == "__main__":
    print(regexer())
