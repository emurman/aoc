#!/usr/bin/python3

from pathlib import Path
import sys
import stat

year = sys.argv[1]
for i in range(1, 25):
    scriptFileName = f"{year}/{i}.py"
    f = open(scriptFileName, "x")
    f.write(
        f'''#!/usr/bin/python3

from io import TextIOWrapper

useSample = True

def part1(f: TextIOWrapper):
    result = 0

    for line in f.readlines():
        pass
    
    print(f"Result: {{result}}")

def part2(f: TextIOWrapper):
    result = 0

    for line in f.readlines():
        pass

    print(f"Result: {{result}}")

problem = "{i}"
year = "{year}"
sample = f"{{year}}/{{problem}}.example.txt"
puzzleInput = f"{{year}}/{{problem}}.txt"

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
'''
    )
    f.close()
    f = Path(scriptFileName)
    f.chmod(f.stat().st_mode | stat.S_IEXEC)

    f = open(f"{year}/{i}.example.txt", "x")
    f.close()
    f = open(f"{year}/{i}.txt", "x")
    f.close()
