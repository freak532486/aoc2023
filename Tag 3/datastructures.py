class CharField:
    def __init__(self, input_string: str):
        lines = input_string.splitlines()

        self.width  = len(lines[0])
        self.height = len(lines)
        self.lines  = lines

    def getCharAt(self, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.height:
            return '.'

        return self.lines[y][x]
    
class FieldNumber:

    def __init__(self, xmin, xmax, y, number):
        self.xmin   = xmin
        self.xmax   = xmax
        self.y      = y
        self.number = number

    def __str__(self):
        return f"{self.number} at ({self.xmin}..{self.xmax}, {self.y})"
    
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"