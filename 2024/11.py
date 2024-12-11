#!/usr/bin/python3

from io import TextIOWrapper
from math import floor, log10

useSample = False

def parse(f: TextIOWrapper):
    result = None

    for line in f.readlines():
        return [int(num) for num in line.strip().split()]

    return result

def part1(parsedInput):
    result = 0
    def blink(rocks):
        result = []
        for rock in rocks:
            rockStr = str(rock)
            if rock == 0:
                result.append(1)
            elif len(rockStr) % 2 == 0:
                halfway = len(rockStr) // 2
                result.append(int(rockStr[:halfway]))
                result.append(int(rockStr[halfway:]))
            else:
                result.append(2024 * rock)
        
        return result
    
    rocks = parsedInput
    for _ in range(25):
        rocks = blink(rocks)

    result = len(rocks)
    print(f"Result: {result}")

def part2(parsedInput):
    result = 0
    cache = dict()

    def count(num, depth):
        if (num, depth) in cache:
            return cache[(num, depth)]
        if depth == 0: return 1
        if num == 0: return count(1, depth - 1)

        digits = floor(log10(num)) + 1
        if digits % 2 != 0: 
            result = count(num * 2024, depth - 1)
            cache[(num, depth)] = result
            return result

        result = (count(num // 10 ** (digits // 2), depth - 1) +
                count(num % 10 ** (digits // 2), depth - 1))
        
        cache[(num, depth)] = result
        return result
    
    result = sum(count(rock, 75) for rock in parsedInput)
    print(f"Result: {result}")

problem = "11"
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
