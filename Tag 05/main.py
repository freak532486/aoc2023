from datastructures import *
from utils import *

# constants
LINE_IDX_SEEDS                   = 0
LINE_IDX_SEED_TO_SOIL            = 3
LINE_IDX_SOIL_TO_FERTILIZER      = 38
LINE_IDX_FERTILIZER_TO_WATER     = 64
LINE_IDX_WATER_TO_LIGHT          = 88
LINE_IDX_LIGHT_TO_TEMPERATURE    = 109
LINE_IDX_TEMPERATURE_TO_HUMIDITY = 122
LINE_IDX_HUMIDITY_TO_LOCATION    = 133

# read input file
f = open("input.txt")
lines = f.read().splitlines()
f.close()

# parse input file
seeds = parse_seeds_line(lines[LINE_IDX_SEEDS])

seed_to_soil            = parse_map_block(lines, LINE_IDX_SEED_TO_SOIL)
soil_to_fertilizer      = parse_map_block(lines, LINE_IDX_SOIL_TO_FERTILIZER)
fertilizer_to_water     = parse_map_block(lines, LINE_IDX_FERTILIZER_TO_WATER)
water_to_light          = parse_map_block(lines, LINE_IDX_WATER_TO_LIGHT)
light_to_temperature    = parse_map_block(lines, LINE_IDX_LIGHT_TO_TEMPERATURE)
temperature_to_humidity = parse_map_block(lines, LINE_IDX_TEMPERATURE_TO_HUMIDITY)
humidity_to_location    = parse_map_block(lines, LINE_IDX_HUMIDITY_TO_LOCATION)

maps = [
    seed_to_soil,
    soil_to_fertilizer,
    fertilizer_to_water,
    water_to_light,
    light_to_temperature,
    temperature_to_humidity,
    humidity_to_location
]

# propagate each seed
min = 9999999999999999999
for seed in seeds:
    cur_min = find_min_in_ival_list(do_multiple_propagation(seed, maps))
    if cur_min < min:
        min = cur_min

print(min)