from datastructures import *
from util import *

# read input file
f = open("input.txt")
lines = f.read().splitlines()
f.close()

lines.append("")

# Parse into fields
fields = []

curField = None

for line in lines:
    if len(line) == 0:
        fields.append(curField)
        curField = None
        continue

    if curField == None:
        curField = TextField(len(line))

    curField.addRow(line)

# Find mirror lines for each field
sum = 0
for field in fields:
    horMirror = findHorizontalMirrorLine(field)
    verMirror = findVerticalMirrorLine(field)

    if horMirror != -1:
        print(f"Horizontal mirror at y = {horMirror}")
        sum += 100 * horMirror
    elif verMirror != -1:
        print(f"Vertical mirror at x = {verMirror}")
        sum += verMirror
    else:
        print(f"found no reflection for: \n{field}")

print(sum)