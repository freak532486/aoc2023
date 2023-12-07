from datastructures import *


def propagate_interval(ival: Interval, map: list) -> list:
    ret = []
    mapped = []

    for key_ival in map:
        if interval_contains(ival, key):
            ret.append(map[key])
            mapped.append(key)
    
    for i in range(len(mapped) + 1):
        lo = ival.lo if i == 0 else mapped[i - 1] + 1
        hi = ival.hi if i == len(mapped) else mapped[i] - 1

        if lo > hi:
            continue

        ret.append(Interval(lo, hi))
    
    return ret

def propagate_interval_list(ival_list: list, map: dict) -> list:
    ret = []
    for ival in ival_list:
        ret.extend(propagate_interval(ival, map))
    return ret

def do_multiple_propagation(seed: int, maps: list) -> list:
    cur = [Interval(seed, seed)]

    for map in maps:
        print(cur)
        cur = propagate_interval_list(cur, map)
    
    print(cur)
    print("")
    
    return cur

def find_min_in_ival_list(ival_list: list) -> int:
    min = ival_list[0].lo
    for i in range(1, len(ival_list)):
        if list[i].lo < min:
            min = ival_list[i].lo
    return min


def parse_seeds_line(line: str) -> list:
    r = line.split(":")[1].strip()
    return list(map(lambda x : int(x), r.split()))

def parse_map_line(line: str, map: list):
    split = line.split()

    src_lo = int(split[0])
    dst_lo = int(split[1])
    range  = int(split[2])

    src_ival = Interval(src_lo, src_lo + range)
    dst_ival = Interval(dst_lo, dst_lo + range)
    map.append(IntervalPair(src_ival, dst_ival))

def parse_map_block(lines: str, first_line_idx: int) -> dict:
    map = list()
    i = first_line_idx
    while i < len(lines):
        line = lines[i]
        if len(line) == 0:
            break

        parse_map_line(line, map)
        i += 1
    
    return map



def interval_contains(ival: Interval, x: int):
    return x >= ival.lo and x <= ival.hi

def interval_list_contains(ival_list: list, x: int):
    for ival in ival_list:
        if interval_contains(ival, x):
            return True
    return False