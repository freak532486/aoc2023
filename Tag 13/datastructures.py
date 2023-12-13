class TextField:
    def __init__(self, width: int):
        self.width = width
        self.height = 0
        self.data = []

    def addRow(self, data: list):
        assert(len(data) == self.width)
        
        for c in data:
            self.data.append(c)
        
        self.height += 1

    def getRow(self, y: int) -> list:
        beg = y * self.width
        end = (y + 1) * self.width
        return self.data[beg:end]
    
    def getCol(self, x: int) -> list:
        col = []
        for y in range(self.height):
            col.append(self.data[x + y * self.width])
        return col
    
    def __repr__(self) -> str:
        ret = ""
        for y in range(self.height):
            for x in range(self.width):
                ret += self.data[x + y * self.width]
            ret += "\n"
        return ret
    