#!/usr/bin/python3

from io import TextIOWrapper

useSample = True

def parse(f: TextIOWrapper):
    result = None

    for line in f.readlines():
        pass

    return result

def part1(parsedInput):
    result = 0

    print(f"Result: {result}")

def part2(parsedInput):
    result = 0

    print(f"Result: {result}")

problem = "7"
year = "2024"
sample = f"{year}/{problem}.example.txt"
puzzleInput = f"{year}/{problem}.txt"

usedInput = sample if useSample else puzzleInput

if useSample:
    print("Running with sample input")
else:
    print("Running with actual input")

print()
parsedInput = None

with open(usedInput) as f:
    print("Part 1")
    parsedInput = parse(f)
    part1(parsedInput)

    print()
    print("Part 2")
    part2(parsedInput)
