from datastructures import *
from utils import *
from functools import cmp_to_key

# read input file
f = open("input.txt")
lines = f.read().splitlines()
f.close()

pairs = []
for line in lines:
    spl = line.split()

    hand = strToHand(spl[0])
    bid  = int(spl[1])
    pairs.append(HandBidPair(hand, bid))

# Sort pairs by value
pairs.sort(key = cmp_to_key(lambda p1, p2 : compareHands(p1.hand, p2.hand)))

sum = 0
for i in range(len(pairs)):
    sum += (i + 1) * pairs[i].bid

print(sum)