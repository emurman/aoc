#!/usr/bin/python3

import heapq
from io import TextIOWrapper

useSample = True

def part1(f: TextIOWrapper):
    result = 0

    left, right = [], []

    for line in f.readlines():
        l, r = [int(num) for num in line.split()]
        heapq.heappush(left, l)
        heapq.heappush(right, r)
    
    while left:
        result += abs(heapq.heappop(left) - heapq.heappop(right))
    
    print(f"Result: {result}")

def part2(f: TextIOWrapper):
    result = 0

    for line in f.readlines():
        pass

    print(f"Result: {result}")

problem = "1"
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
