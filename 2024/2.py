#!/usr/bin/python3

from io import TextIOWrapper

useSample = False

def solve(report):
    if len(report) == 1:
        result += 1
    
    isAscending = report[0] < report[1]
    isSafe = True
    for level in range(1, len(report)):
        diff = report[level] - report[level - 1]
        if abs(diff) > 3 or diff == 0:
            isSafe = False
            break
            
        if (diff > 0 and not isAscending) or (diff < 0 and isAscending):
            isSafe = False
            break
        
    return 1 if isSafe else 0

def part1(f: TextIOWrapper):
    result = 0
    reports = []

    for line in f.readlines():
        reports.append([int(num) for num in line.split()])

    for report in reports:
        result += solve(report)

    print(f"Result: {result}")

def part2(f: TextIOWrapper):
    result = 0
    reports = []

    for line in f.readlines():
        reports.append([int(num) for num in line.split()])

    for report in reports:
        if len(report) == 1:
            result += 1
        
        for i in range(len(report)):
            if solve(report[:i] + report[i + 1:]):
                result += 1
                break

    print(f"Result: {result}")

problem = "2"
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
