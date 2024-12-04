#!/usr/bin/python3

from io import TextIOWrapper
import re

useSample = False

def part1(f: TextIOWrapper):
    result = 0

    pattern = re.compile(r"(mul\(\d{1,3},\d{1,3}\))")
    for line in f.readlines():
        for match in pattern.finditer(line):
            mult = match.group(1)
            mult = [int(num) for num in mult[4:-1].split(",")]
            result += mult[0] * mult[1]
    
    print(f"Result: {result}")

def part2(f: TextIOWrapper):
    result = 0

    pattern = re.compile(r"(do\(\))|(don't\(\))|(mul\(\d{1,3},\d{1,3}\))")
    shouldDo = True

    for line in f.readlines():
        for match in pattern.finditer(line):
            do, doNot, mult = match.groups()
            if doNot is not None:
                shouldDo = False
            elif do is not None:
                shouldDo = True
            elif shouldDo:
                mult = [int(num) for num in mult[4:-1].split(",")]
                result += mult[0] * mult[1]

    print(f"Result: {result}")

problem = "3"
year = "2024"
sample = f"{year}/{problem}.example.txt"
puzzleInput = f"{year}/{problem}.txt"

usedInput = sample if useSample else puzzleInput

if useSample:
    print("Running with sample input")
else:
    print("Running with actual input")

print()

with open(usedInput) as f:
    print("Part 1")
    part1(f)

print()

with open(usedInput) as f:
    print("Part 2")
    part2(f)
