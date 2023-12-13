from datastructures import *
from util import *

# Read input file
f = open("input.txt")
lines = f.read().splitlines()
f.close()

# Convert to universe
universe = Universe(lines)

print(universe)
print("")

# Find empty rows and columns
emptyX = []
for x in range(universe.getWidth()):
    if hasNoGalaxy(universe.getColumn(x)):
        emptyX.append(x)

emptyY = []
for y in range(universe.getHeight()):
    if hasNoGalaxy(universe.getRow(y)):
        emptyY.append(y)

# Find all galaxies
galaxies = []
for y in range(universe.getHeight()):
    for x in range(universe.getWidth()):
        if universe.getCharAt(x, y) == '#':
            galaxies.append((x, y))

# Calculate result
sum = 0
for i in range(len(galaxies)):
    for j in range(i, len(galaxies)):
        a: tuple = galaxies[i]
        b: tuple = galaxies[j]
        sum += manhattanDist(a, b, emptyX, emptyY)

print(sum)