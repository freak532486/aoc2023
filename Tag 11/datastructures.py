class Universe:
    def __init__(self, inputLines: list):
        self.width = len(inputLines[0])
        self.height = len(inputLines)

        self.charArr = []
        for line in inputLines:
            for c in line:
                self.charArr.append(c)
    
    def getCharAt(self, x: int, y: int) -> chr:
        return self.charArr[x + y * self.width]
    
    def getRow(self, y: int) -> list:
        row = []
        for x in range(self.width):
            row.append(self.getCharAt(x, y))
        return row
    
    def getColumn(self, x: int) -> list:
        col = []
        for y in range(self.height):
            col.append(self.getCharAt(x, y))
        return col
    
    # Adds row _below_ row at given y
    def addRow(self, y: int, rowChar: chr):
        rowStart = (y + 1) * self.width
        for x in range(self.width):
            self.charArr.insert(rowStart + x, rowChar)
        self.height += 1

    # Adds column _to the right_ of row at given x
    def addCol(self, x: int, colChar: chr):
        for y in range(self.height):
            self.charArr.insert(x + y * (self.width + 1) + 1, colChar)
        self.width += 1

    def getWidth(self) -> int:
        return self.width
    
    def getHeight(self) -> int:
        return self.height
    
    def __repr__(self):
        ret = ""
        for y in range(self.getHeight()):
            for x in range(self.getWidth()):
                ret += self.getCharAt(x, y)
            ret += "\n"
        return ret