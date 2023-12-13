def getDigits(line):
    ret = []
    for i in range(0, len(line)):
        if line.startswith("zero" , i) or line.startswith("0", i): ret.append(0)
        if line.startswith("one"  , i) or line.startswith("1", i): ret.append(1)
        if line.startswith("two"  , i) or line.startswith("2", i): ret.append(2)
        if line.startswith("three", i) or line.startswith("3", i): ret.append(3)
        if line.startswith("four" , i) or line.startswith("4", i): ret.append(4)
        if line.startswith("five" , i) or line.startswith("5", i): ret.append(5)
        if line.startswith("six"  , i) or line.startswith("6", i): ret.append(6)
        if line.startswith("seven", i) or line.startswith("7", i): ret.append(7)
        if line.startswith("eight", i) or line.startswith("8", i): ret.append(8)
        if line.startswith("nine" , i) or line.startswith("9", i): ret.append(9)
    return ret

f = open("input.txt", "r")
lines = f.readlines()

sum = 0
for line in lines:
    digits = getDigits(line)
    sum += 10 * digits[0] + digits[-1]

print(sum)
            