# read input file
f = open("input.txt")
lines = f.readlines()
f.close()

class Draw:
    def __init__(self):
        self.r = 0
        self.g = 0
        self.b = 0

# go line by line
sum = 0
i   = 1

for line in lines:
    r = line.split(":")[1].strip()
    draws = r.split(";")

    min_r = 0
    min_g = 0
    min_b = 0

    for draw in draws:
        draw = draw.strip()
        balls = draw.split(", ")

        d = Draw()
        for ball in balls:
            amount = int(ball.split()[0])
            color  = ball.split()[1]

            if color == "red":
                d.r += amount
            elif color == "green":
                d.g += amount
            elif color == "blue":
                d.b += amount
        
        min_r = max(min_r, d.r)
        min_g = max(min_g, d.g);
        min_b = max(min_b, d.b);
    
    sum += min_r * min_g * min_b

print(sum)