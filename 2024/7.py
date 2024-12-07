#!/usr/bin/python3

from io import TextIOWrapper
from multiprocessing import cpu_count, Pool

useSample = False

def parse(f: TextIOWrapper):
    result = []

    for line in f.readlines():
        target, nums = line.split(":")
        nums = [int(num) for num in nums.strip().split(" ")]
        target = int(target)
        result.append((target, nums))

    return result

def backtrack(i, nums, target, acc, operators):
    if i == len(nums):
        return target if acc == target else 0

    if acc > target: return 0

    for operator in operators:
        newAcc = operator(acc, nums[i])
        if backtrack(i + 1, nums, target, newAcc, operators):
            return target
    
    return 0

addition = lambda x, y: x + y
multiplication = lambda x, y: x * y
concatenation = lambda x, y: int(str(x) + str(y))

def part1(parsedInput):
    result = 0
    
    for equation in parsedInput:
        target, nums = equation
        result += backtrack(1, nums, target, nums[0], [addition, multiplication])

    print(f"Result: {result}")

def process(equation):
    target, nums = equation
    return backtrack(1, nums, target, nums[0], [addition, multiplication, concatenation])

def part2(parsedInput):
    result = 0
    pool = Pool(cpu_count() - 1)

    result = sum(pool.map(process, parsedInput))

    print(f"Result: {result}")

if __name__ == "__main__":
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
