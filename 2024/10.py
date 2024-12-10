#!/usr/bin/python3

from collections import deque
from io import TextIOWrapper

useSample = False

def parse(f: TextIOWrapper):
    result = []

    for line in f.readlines():
        result.append([int(num) for num in line.strip()])

    return result

directions = [
    (0, 1),
    (1, 0),
    (0, -1),
    (-1, 0)
]

def part1(parsedInput):
    result = 0
    grid = parsedInput

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != 0: continue
            visited = set()
            queue = deque()
            queue.append((i, j))

            while queue:
                elem = queue.popleft()
                if elem in visited: continue
                visited.add(elem)

                value = grid[elem[0]][elem[1]]
                if value == 9: 
                    result += 1
                    continue


                for di, dj in directions:
                    newI, newJ = elem[0] + di, elem[1] + dj
                    if newI < 0 or newI >= len(grid) or newJ < 0 or newJ >= len(grid[i]): continue

                    if grid[newI][newJ] == value + 1:
                        queue.append((newI, newJ))

    print(f"Result: {result}")

def part2(parsedInput):
    result = 0
    grid = parsedInput
    dp_cache = {}

    def dp(i, j):
        if grid[i][j] == 0: return 1
        if (i, j) in dp_cache: return dp_cache[(i, j)]

        result = 0
        for di, dj in directions:
            newI, newJ = i + di, j + dj
            if newI < 0 or newI >= len(grid) or newJ < 0 or newJ >= len(grid[i]): continue

            if grid[newI][newJ] == grid[i][j] - 1:
                result += dp(newI, newJ)

        dp_cache[(i, j)] = result
        return result
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 9:
                result += dp(i, j)

    print(f"Result: {result}")

problem = "10"
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
