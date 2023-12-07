from datastructures import *

def parse_mapping_line(line: str) -> Mapping:
    spl = line.split()
    return Mapping(int(spl[1]), int(spl[0]), int(spl[2]))

def parse_mapping_block(lines: list, first_line_idx: int) -> list:
    ret = []
    i = first_line_idx
    while i < len(lines):
        line = lines[i]

        if len(line) == 0:
            break

        ret.append(parse_mapping_line(line))
        i += 1
    
    return ret


def apply_mappings(x: int, mappings: list):
    ret = None
    for mapping in mappings:
        ret = mapping.map(x)
        if ret != None:
            break

    if ret == None:
        ret = x

    return ret

def apply_mappings_ival(ival: Interval, mappings: list):
    ret = []
    mapped = []
    for mapping in mappings:
        isect = ival_isect(ival, mapping.src_ival())

        if isect == None:
            continue

        ret.append(Interval(isect.lo + mapping.offset(), isect.hi + mapping.offset()))
        mapped.append(isect)
    
    mapped.sort(key = lambda ival : ival.lo)

    for i in range(len(mapped) + 1):
        lo = ival.lo if i == 0 else mapped[i - 1].hi + 1
        hi = ival.hi if i == len(mapped) else mapped[i].lo - 1

        if lo > hi:
            continue

        ret.append(Interval(lo, hi))
    
    return ret


def ival_isect(a: Interval, b: Interval):
    lo = max(a.lo, b.lo)
    hi = min(a.hi, b.hi)

    if lo > hi:
        return None

    return Interval(lo, hi)