from datastructures import *

# read input file
f = open("input.txt")
lines = f.read().splitlines()
f.close()

# Parse races
spl1 = lines[0].split()
spl2 = lines[1].split()
races = [
    Race(int(spl1[1]), int(spl2[1])),
    Race(int(spl1[2]), int(spl2[2])),
    Race(int(spl1[3]), int(spl2[3])),
    Race(int(spl1[4]), int(spl2[4])),
]

# Parse the big race
big_race = Race(int(spl1[1] + spl1[2] + spl1[3] + spl1[4]), int(spl2[1] + spl2[2] + spl2[3] + spl2[4]))

# solution for single race
def calcPossibilities(race: Race) -> int:
    ret = 0
    for i in range(race.duration):
        speed     = i
        remaining = race.duration - i
        distance  = speed * remaining

        if distance > race.record:
            ret += 1
    
    return ret

# Solve all four races
solution = calcPossibilities(races[0]) \
         * calcPossibilities(races[1]) \
         * calcPossibilities(races[2]) \
         * calcPossibilities(races[3])

# Solve big race
big_solution = calcPossibilities(big_race)

print(big_solution)