class DescriptorRow:
    STATE_OPERATIONAL = 0
    STATE_BROKEN = 1
    STATE_UNKNOWN = 2

    def __init__(self, line: str):
        lhs = line.split()[0]
        rhs = line.split()[1]

        # parse LHS
        self.springStates = []
        for i in range(len(line)):
            match (line[i]):
                case '.': self.springStates.append(DescriptorRow.STATE_OPERATIONAL)
                case '#': self.springStates.append(DescriptorRow.STATE_BROKEN)
                case '?': self.springStates.append(DescriptorRow.STATE_UNKNOWN)
        
        # parse RHS
        rhsSplit = rhs.split(",")
        self.springNumbers = []
        for s in rhsSplit:
            self.springNumbers.append(int(s))

    def getNumUnknown(self):
        sum = 0
        for state in self.springStates:
            if state == DescriptorRow.STATE_UNKNOWN:
                sum += 1
        return sum
    
    def getLength(self):
        return len(self.springStates)

class RowAttempt:
    def __init__(self, row: DescriptorRow):
        self.row = row
        self.attemptedSpringStates = [DescriptorRow.STATE_UNKNOWN] * row.getLength()

    def getStateAtIdx(self, i: int) -> int:
        return self.row.springStates[i] if self.row.springStates[i] != DescriptorRow.STATE_UNKNOWN else self.attemptedSpringStates[i]
    
    def putAttempt(self, idx: int, state: int):
        self.attemptedSpringStates[idx] = state

    def isValid(self) -> bool:
        curNumberIdx = 0
        curChainLength = 0

        for i in range(len(self.row.springStates)):
            state = self.getStateAtIdx(i)

            if state == DescriptorRow.STATE_OPERATIONAL and curChainLength == 0:
                continue

            if state == DescriptorRow.STATE_BROKEN and curChainLength > 0:
                curChainLength += 1
                continue

            if state == DescriptorRow.STATE_BROKEN and curChainLength == 0:
                if curNumberIdx >= len(self.row.springNumbers):
                    return False

                curChainLength += 1
                continue

            if state == DescriptorRow.STATE_OPERATIONAL and curChainLength > 0:
                if curChainLength != self.row.springNumbers[curNumberIdx]:
                    return False
                
                curChainLength = 0
                curNumberIdx += 1
        
        if self.getStateAtIdx(self.row.getLength() - 1) == DescriptorRow.STATE_BROKEN:
            if curChainLength != self.row.springNumbers[curNumberIdx]:
                return False
            
            curNumberIdx += 1

        if curNumberIdx != len(self.row.springNumbers):
            return False
        
        return True
    
    def __repr__(self) -> str:
        ret = "Attempt "
        for i in range(len(self.row.springStates)):
            state = self.getStateAtIdx(i)
            ret += '#' if state == DescriptorRow.STATE_BROKEN else '.'
        ret += " for numbers "
        for num in self.row.springNumbers:
            ret += str(num) + " "
        ret += "is " + ("valid" if self.isValid() else "not valid")
        return ret