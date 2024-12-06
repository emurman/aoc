#!/usr/bin/python3

from io import TextIOWrapper

useSample = False

def parse(f: TextIOWrapper):
    grid = []
    startingPos = None

    for i, line in enumerate(f.readlines()):
        grid.append([])
        for j, cell in enumerate(line.strip()):
            if cell == "^":
                startingPos = i, j
                grid[-1].append(".")
            else:
                grid[-1].append(cell)

    return grid, startingPos

def turnRight(direction):
    di = 0 if direction[1] == 0 else direction[1]
    dj = 0 if direction[0] == 0 else -direction[0]
    return di, dj

def part1(parsedInput):
    result = 0
    grid, (i, j) = parsedInput
    direction = (-1, 0)
    visited = set()
    visited.add((i, j))

    while True:
        nextI, nextJ = i + direction[0], j + direction[1]
        if nextI < 0 or nextI >= len(grid) or nextJ < 0 or nextJ >= len(grid[0]):
            break

        if grid[nextI][nextJ] == "#":
            direction = turnRight(direction)
            continue

        i, j = nextI, nextJ
        visited.add((i, j))
    
    result = len(visited)
    print(f"Result: {result}")

def part2(parsedInput):
    result = 0
    grid, (i, j) = parsedInput
    direction = (-1, 0)
    visited = set()
    visited.add((i, j) + direction)

    for k in range(len(grid)):
        print(f"Row {k + 1} / {len(grid)}")

        for l in range(len(grid[0])):
            if grid[k][l] == "#" or (k, l) == parsedInput[1]: continue
            grid[k][l] = "0"

            i, j = parsedInput[1]
            direction = (-1, 0)
            visited = set()
            visited.add((i, j) + direction)

            while True:
                nextI, nextJ = i + direction[0], j + direction[1]
                if nextI < 0 or nextI >= len(grid) or nextJ < 0 or nextJ >= len(grid[0]):
                    break

                if (nextI, nextJ) + direction in visited:
                    result += 1
                    break

                if grid[nextI][nextJ] == "#" or grid[nextI][nextJ] == "0":
                    direction = turnRight(direction)
                    continue

                i, j = nextI, nextJ
                visited.add((i, j) + direction)
            grid[k][l] = "."

    print(f"Result: {result}")

problem = "6"
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
