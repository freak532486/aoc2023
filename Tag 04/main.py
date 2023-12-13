# read input
f = open("input.txt")
lines = f.readlines()
f.close()

points = 0
num_cards = [1] * len(lines)

for i in range(len(lines)):
    line = lines[i]

    fullcard = line.split(":")[1].strip()

    winners_str = fullcard.split("|")[0].strip()
    numbers_str = fullcard.split("|")[1].strip()

    winners = list(map(lambda x : int(x), winners_str.split()))
    numbers = list(map(lambda x : int(x), numbers_str.split()))

    intersection = [x for x in winners if x in numbers]
    num_winners = len(intersection)

    if num_winners == 0:
        continue

    for j in range(i + 1, i + 1 + num_winners):
        num_cards[j] += num_cards[i]

print(sum(num_cards))