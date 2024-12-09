#!/usr/bin/python3

from io import TextIOWrapper
from math import ceil

useSample = False

class Node:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.next = None
        self.prev = None
    
    def __repr__(self):
        return f"Node({self.value})"

def parse(f: TextIOWrapper):
    l = None
    for line in f.readlines():
        l = [int(x) for x in line.strip()]

    head = Node(None, -1)
    current = head
    i = 0
    outputIndex = 0
    fileId = 0

    while i < len(l):
        for _ in range(l[i]):
            newNode = Node(fileId, outputIndex)
            outputIndex += 1
            current.next = newNode
            newNode.prev = current
            current = newNode
        fileId += 1

        if i + 1 >= len(l):
            break

        for _ in range(l[i + 1]):
            newNode = Node(None, outputIndex)
            outputIndex += 1
            current.next = newNode
            newNode.prev = current
            current = newNode

        i += 2
    
    return head, current


def calculateChecksum(node):
    current = node
    result = 0
    while current:
        if current.value is not None:
            result += current.index * current.value
        current = current.next
    return result

def part1(parsedInput):
    result = 0
    head, tail = parsedInput
    start, end = head.next, tail

    while start != end:
        if start.value is None:
            start.value = end.value
            end.value = None
            end = end.prev
            continue

        start = start.next

    result = calculateChecksum(head.next)

    return result

def part2(parsedInput):
    result = 0
    head, tail = parsedInput

    def findSequenceOfLength(node, length, cutOff):
        current = node

        while current:
            while current and current.value is not None:
                if current.value == cutOff: return None
                current = current.next
            
            if not current:
                return None
            
            start = current
            i = 0
            while i < length and current and current.value is None:
                current = current.next
                i += 1
            
            if i == length:
                return start

        return None

    end = tail
    print("Moving backwards through the input...")
    lastProgressPercent = None

    # This is so horrific but I'm too tired to improve it
    while end != head:
        progressPercent = ceil(100 - (end.index / tail.index) * 100)
        if lastProgressPercent is None:
            lastProgressPercent = progressPercent
        
        if progressPercent != lastProgressPercent:
            print(f"progress: {progressPercent} %")
            lastProgressPercent = progressPercent
            
        # Find the next file from the end
        if end.value is None:
            end = end.prev
            continue

        fileId = end.value
        count = 0
        endIter = end
        # Find the length of the file
        while endIter and endIter.value == fileId:
            count += 1
            endIter = endIter.prev
        
        # Find the first spot the file could be moved to
        sequenceStart = findSequenceOfLength(head.next, count, fileId)
        if sequenceStart is None:
            end = endIter
            continue

        i = 0
        # "Debit" and "Credit" the file
        while i < count:
            sequenceStart.value = fileId
            sequenceStart = sequenceStart.next
            end.value = None
            end = end.prev
            i += 1

    result = calculateChecksum(head.next)

    return result

problem = "9"
year = "2024"
sample = f"{year}/{problem}.example.txt"
puzzleInput = f"{year}/{problem}.txt"

usedInput = sample if useSample else puzzleInput

parsedInput = None

with open(usedInput) as f:
    print("Part 1")
    parsedInput = parse(f)
    p1result = part1(parsedInput)

with open(usedInput) as f:
    print("Part 2")
    parsedInput = parse(f)
    p2result = part2(parsedInput)
    print("Part 1 result:", p1result)
    print("Part 2 result:", p2result)

