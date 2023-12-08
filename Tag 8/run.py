class Node:
    def __init__(self, id: int, label: str):
        self.id    = id
        self.label = label
        self.left  = None
        self.right = None

    def __repr__(self):
        return f"{self.label} -> ({self.left.label}, {self.right.label})"
    
class Cycle:
    def __init__(self, cycleAfter, cycleLen, goalNodeIndices):
        self.cycleAfter      = cycleAfter
        self.cycleLen        = cycleLen
        self.goalNodeIndices = goalNodeIndices

    def __repr__(self):
        return f"Cycle after {self.cycleAfter} steps with length {self.cycleLen} with goal indices {self.goalNodeIndices}"

# read input
f = open("input.txt")
lines = f.read().splitlines()
f.close()

# read graph
labelToNodeId = {}
nodes = []
curMaxId = 0

def getOrRegisterNode(label: str) -> Node:
    global curMaxId
    global labelToNodeId
    global nodes

    if label not in labelToNodeId:
        labelToNodeId[label] = curMaxId
        nodes.append(Node(curMaxId, label))
        curMaxId += 1
    
    return nodes[labelToNodeId[label]]

startNodes = []

for i in range(2, len(lines)):
    line = lines[i]
    spl = line.split(" = ")

    # Register node on left side of equal sign
    lhs = spl[0]

    lhsNode = getOrRegisterNode(lhs)

    if lhsNode.label[2] == 'A':
        startNodes.append(lhsNode)

    # Register two children
    rhs = spl[1]

    childLabel1 = rhs.split(", ")[0][1:]
    childLabel2 = rhs.split(", ")[1][:-1]

    childNode1 = getOrRegisterNode(childLabel1)
    childNode2 = getOrRegisterNode(childLabel2)

    lhsNode.left = childNode1
    lhsNode.right = childNode2

# Read instructions
instr = lines[0]

# Run until done
curNodes: list = list(startNodes)
numSteps = 0

# Testing


def test(n: int):
    curNode = curNodes[n]
    visited = [curNode]
    cycle: Cycle = None
    i = 0
    while True:
        curInstr = instr[i % len(instr)]

        if curInstr == "L":
            curNode = curNode.left
        else:
            curNode = curNode.right

        i += 1

        done = False
        for j in range(len(visited)):
            if visited[j] == curNode and j % len(instr) == i % len(instr):
                cycleAfter = j
                cycleLen   = i - j
                goalNodeIndices = []

                for k in range(j, len(visited)):
                    if visited[k].label[2] == 'Z':
                        print(f"{visited[k].label} at k = {k}")
                        goalNodeIndices.append(k - cycleAfter)

                cycle = Cycle(cycleAfter, cycleLen, goalNodeIndices)

                done = True
                break
        
        if done:
            break

        visited.append(curNode)
    return cycle


for i in range(len(curNodes)):
    print(test(i))