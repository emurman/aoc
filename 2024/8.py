#!/usr/bin/python3

from collections import defaultdict
from io import TextIOWrapper

useSample = False

def parse(f: TextIOWrapper):
    grid = []
    antennas = defaultdict(list)

    for line in f.readlines():
        grid.append([c for c in line.strip()])

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.': continue
            antennas[grid[i][j]].append((i, j))

    return grid, antennas

def isInBounds(node, grid):
    return node[0] >= 0 and node[0] < len(grid) and node[1] >= 0 and node[1] < len(grid[node[0]])

def part1(parsedInput):
    result = 0
    nodes = set()
    grid, antennas = parsedInput

    for antenna in antennas.values():
        for i in range(len(antenna)):
            for j in range(i + 1, len(antenna)):
                a1, a2 = antenna[i], antenna[j]
                di, dj = a1[0] - a2[0], a1[1] - a2[1] 
                node1, node2 = (a1[0] + di, a1[1] + dj), (a2[0] - di, a2[1] - dj)
                for node in [node1, node2]:
                    if not isInBounds(node, grid): continue
                    nodes.add(node)

    result = len(nodes)
    print(f"Result: {result}")

def part2(parsedInput):
    result = 0
    grid, antennas = parsedInput
    nodes = set()

    for antenna in antennas.values():
        for i in range(len(antenna)):
            for j in range(i + 1, len(antenna)):
                # Expand outwards from both antennas
                node1, node2 = antenna[i], antenna[j]
                di, dj = node1[0] - node2[0], node1[1] - node2[1] 

                while True:
                    eitherInBounds = False
                    if isInBounds(node1, grid):
                        nodes.add(node1)
                        eitherInBounds = True
                    if isInBounds(node2, grid):
                        nodes.add(node2)
                        eitherInBounds = True
                    
                    if not eitherInBounds: break
                    node1, node2 = (node1[0] + di, node1[1] + dj), (node2[0] - di, node2[1] - dj)

    result = len(nodes)
    print(f"Result: {result}")

problem = "8"
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
