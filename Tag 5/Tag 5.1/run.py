from utils import *

# read input file
f = open("input.txt")
lines = f.read().splitlines()
f.close()

# parse seeds
r = lines[0].split(":")[1].strip()
split = r.split()
seeds = list(map(lambda x : int(x), split))

# parse seeds as intervals
seed_ivals = []
for i in range(0, len(split), 2):
    lo = int(split[i])
    hi = lo + int(split[i + 1]) - 1
    seed_ivals.append(Interval(lo, hi))

# parse all mapping blocks
LINENO_SEED_TO_SOIL = 3
LINENO_SOIL_TO_FERT = 38
LINENO_FERT_TO_WATR = 64
LINENO_WATR_TO_LGHT = 88
LINENO_LGHT_TO_TEMP = 109
LINENO_TEMP_TO_HMTY = 122
LINENO_HMTY_TO_LOCA = 133

# LINENO_SEED_TO_SOIL = 3
# LINENO_SOIL_TO_FERT = 7
# LINENO_FERT_TO_WATR = 12
# LINENO_WATR_TO_LGHT = 18
# LINENO_LGHT_TO_TEMP = 22
# LINENO_TEMP_TO_HMTY = 27
# LINENO_HMTY_TO_LOCA = 31

mappings = [
    parse_mapping_block(lines, LINENO_SEED_TO_SOIL),
    parse_mapping_block(lines, LINENO_SOIL_TO_FERT),
    parse_mapping_block(lines, LINENO_FERT_TO_WATR),
    parse_mapping_block(lines, LINENO_WATR_TO_LGHT),
    parse_mapping_block(lines, LINENO_LGHT_TO_TEMP),
    parse_mapping_block(lines, LINENO_TEMP_TO_HMTY),
    parse_mapping_block(lines, LINENO_HMTY_TO_LOCA)
]

# run through every seed interval
min = None
for seed_ival in seed_ivals:
    cur = [ seed_ival ]
    for mapping in mappings:
        print(cur)

        next = []
        for ival in cur:
            next.extend(apply_mappings_ival(ival, mapping))

        cur = next
    
    print(cur)
    print("")
    
    for ival in cur:
        if min == None or ival.lo < min:
            min = ival.lo

print(min)