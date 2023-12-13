EXPAND = 999999

def hasNoGalaxy(input: list) -> bool:
    for c in input:
        if c == '#':
            return False
    return True

def manhattanDist(a: tuple, b: tuple, emptyX: list, emptyY: list) -> int:
    minx = min(a[0], b[0])
    maxx = max(a[0], b[0])
    miny = min(a[1], b[1])
    maxy = max(a[1], b[1])

    dx = 0
    for x in range(minx + 1, maxx + 1):
        if x in emptyX:
            dx += EXPAND + 1
        else:
            dx += 1

    dy = 0
    for y in range(miny + 1, maxy + 1):
        if y in emptyY:
            dy += EXPAND + 1
        else:
            dy += 1

    return dx + dy