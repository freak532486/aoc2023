import copy
from datastructures import *
from util import *
    
def expandLine(line: str):
    lhs = line.split()[0]
    rhs = line.split()[1]

    newLhs = ""
    newRhs = ""

    for i in range(4):
        newLhs += lhs + "?"
        newRhs += rhs + ","

    newLhs += lhs
    newRhs += rhs

    return newLhs + " " + newRhs

# read input
f = open("input.txt")
lines = f.read().splitlines()
f.close()

# handle each line separately
sum = 0
for i in range(len(lines)):
    line: str = expandLine(lines[i])
    
    compStr: str = preprocessInputString(line.split()[0])
    numbers: list = list(map(lambda x : int(x), line.split()[1].split(",")))

    # print(f"Preprocessed input string: {compStr}")

    sum += solveRecursivelyByExtendingGuesses([], compStr, numbers)
    print(f"{i + 1}/{len(lines)}")

print(sum)