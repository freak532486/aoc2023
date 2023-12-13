from datastructures import *

def findNumDifference(list1: list, list2: list):
    total = 0
    for i in range(len(list1)):
        total += (list1[i] != list2[i])
    return total


# Returns -1 when line doesnt exist
def findVerticalMirrorLine(field: TextField) -> int:
    for x in range(1, field.width):
        maxCheck = min(x, field.width - x)
        numErr = 0

        for i in range(maxCheck):
            numErr += findNumDifference(field.getCol(x - i - 1), field.getCol(x + i))
            if numErr > 1:
                break

        if numErr == 1:
            return x
        
    return -1

# Returns -1 when line doesn't exist
def findHorizontalMirrorLine(field: TextField) -> int:
    for y in range(1, field.height):
        maxCheck = min(y, field.height - y)
        numErr = 0

        for i in range(maxCheck):
            numErr += findNumDifference(field.getRow(y - i - 1), field.getRow(y + i))
            if numErr > 1:
                break

        if numErr == 1:
            return y
        
    return -1