import re

from datastructures import *

def is_digit(c):
    return ord(c) >= ord('0') and ord(c) <= ord('9')

def is_symbol(c):
    return not (is_digit(c) or c == '.')

def to_int(c):
    return ord(c) - ord('0')

def is_adjacent(num: FieldNumber, p: Point) -> bool:
    if num.y == p.y:
        if num.xmax == p.x - 1 or num.xmin == p.x + 1:
            return True
        return False
    
    if num.y == p.y - 1 or num.y == p.y + 1:
        if num.xmin <= p.x and num.xmax >= p.x:
            return True
        elif num.xmin == p.x + 1 or num.xmax == p.x - 1:
            return True
        return False
    
    return False

# read input as full string
f = open("input.txt")
input = f.read()
f.close()

# convert to CharField
char_field = CharField(input)

# Find all field numbers in char_field
field_numbers = []
for y in range(char_field.height):
    for x in range(char_field.width):
        c = char_field.getCharAt(x, y)

        if not is_digit(c):
            continue

        if len(field_numbers) > 0 and y == field_numbers[-1].y and x <= field_numbers[-1].xmax:
            continue

        number = to_int(c)
        i = 1
        while True:
            c = char_field.getCharAt(x + i, y)

            if not is_digit(c):
                break

            number = 10 * number + to_int(c)
            i += 1

        field_number = FieldNumber(x, x + i - 1, y, number)
        field_numbers.append(field_number)

# find all gears, sum up their ratios
sum = 0
for y in range(char_field.height):
    for x in range(char_field.width):
        c = char_field.getCharAt(x, y)

        if c != '*':
            continue

        adjacent = []
        p = Point(x, y)

        print(f"Gear at {p}")

        for field_number in field_numbers:
            if is_adjacent(field_number, p):
                adjacent.append(field_number)
        
        print(f"  {len(adjacent)} adjacent field numbers")

        if len(adjacent) != 2:
            continue

        sum += adjacent[0].number * adjacent[1].number

print(sum)
