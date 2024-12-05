#!/usr/bin/python3

from collections import defaultdict
from io import TextIOWrapper

useSample = False

def parse(f: TextIOWrapper):
    rules = []
    updates = []
    parsingRules = True

    for line in f.readlines():
        if not line.strip(): 
            parsingRules = False
            continue

        if parsingRules:
            rules.append([int(num) for num in line.split("|")])
        else:
            updates.append([int(num) for num in line.split(",")])

    return rules, updates

# The full set of rules has cycles, so we can only apply this sort on the subset that is "misplaced" in part 2
# Kinda lame to have to inspect the problem input to figure this out; it's not obvious at all that there happens
# to not be cycles in the misplaced updates
def topologicalSort(rules, whitelist):
    result = []
    inDegree = dict()
    adjMap = defaultdict(list)

    for r1, r2 in rules:
        if r1 not in whitelist or r2 not in whitelist:
            continue

        adjMap[r1].append(r2)
        if r1 not in inDegree:
            inDegree[r1] = 0
        if r2 not in inDegree:
            inDegree[r2] = 1
        else:
            inDegree[r2] += 1
    
    roots = []
    for key, val in inDegree.items():
        if val == 0:
            roots.append(key)
    
    while roots:
        elem = roots.pop()
        result.append(elem)

        for neighbor in adjMap[elem]:
            inDegree[neighbor] -= 1
            if inDegree[neighbor] == 0:
                roots.append(neighbor)
    
    return result

def part1(parsedInput):
    result = 0
    rules, updates = parsedInput
    isBefore = defaultdict(set)
    for r1, r2 in rules:
        isBefore[r2].add(r1)

    for update in updates:
        disallowed = set()
        isValid = True
        for page in update:
            if page in disallowed:
                isValid = False
                break

            if page in isBefore:
                disallowed = disallowed.union(isBefore[page])
        
        if isValid:
            result += update[len(update) // 2]

    print(f"Result: {result}")

def part2(parsedInput):
    result = 0
    rules, updates = parsedInput
    isBefore = defaultdict(list)
    for r1, r2 in rules:
        isBefore[r2].append(r1)

    for update in updates:
        disallowed = defaultdict(list)
        incorrectIndices = set()

        for i, page in enumerate(update):
            if page in disallowed:
                for d in disallowed[page]:
                    incorrectIndices.add(d)
                incorrectIndices.add(i)

            if page in isBefore:
                for before in isBefore[page]:
                    disallowed[before].append(i)

        if not incorrectIndices: continue

        incorrectValues = set()
        for i in incorrectIndices:
            incorrectValues.add(update[i])
        sortedIndices = topologicalSort(rules, incorrectValues)
        j = 0

        for i in range(len(update)):
            if i in incorrectIndices:
                update[i] = sortedIndices[j]
                j += 1
        
        result += update[len(update) // 2]

    print(f"Result: {result}")

problem = "5"
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
