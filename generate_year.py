import sys

year = sys.argv[1]
for i in range(1, 25):
    f = open(f"{year}/{i}.py", "x")
    f.write(
        f'''from io import TextIOWrapper

def part1(f: TextIOWrapper):
    pass

def part2(f: TextIOWrapper):
    pass

input = "{i}.example.txt"
with open(input) as f:
    print("Running part 1")
    part1(f)

with open(input) as f:
    print("Running part 2")
    part2(f)
'''
    )
    f.close()

    f = open(f"{year}/{i}.example.txt", "x")
    f.close()
