#!/usr/bin/python3

from io import TextIOWrapper

useSample = False

cardinals = [
    (0, 1), (0, -1), (1, 0), (-1, 0)
]

diagonals = [
    (1, 1), (-1, -1), (1, -1), (-1, 1)
]

def part1(f: TextIOWrapper):
    result = 0
    grid = []

    for line in f.readlines():
        grid.append([c for c in line.strip()])

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for di, dj in cardinals + diagonals:
                ni, nj = i, j
                isXmas = True
                for c in "XMAS":
                    if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[i]):
                        isXmas = False
                        break
                    if grid[ni][nj] != c:
                        isXmas = False
                        break
                    ni, nj = ni + di, nj + dj
                
                if isXmas:
                    result += 1
    
    print(f"Result: {result}")

def part2(f: TextIOWrapper):
    result = 0

    grid = []

    for line in f.readlines():
        grid.append([c for c in line.strip()])

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != "A": continue

            isInBounds = True
            for di, dj in diagonals:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= len(grid) or nj < 0 or nj >= len(grid[i]):
                    isInBounds = False
                    break
            
            if not isInBounds: continue

            diagOne = grid[i - 1][j - 1] + grid[i + 1][j + 1]
            diagTwo = grid[i - 1][j + 1] + grid[i + 1][j - 1]
            def isMas(s: str) -> bool:
                return s[0] == "M" and s[1] == "S" or s[0] == "S" and s[1] == "M"
            
            if isMas(diagOne) and isMas(diagTwo):
                result += 1

    print(f"Result: {result}")

problem = "4"
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
