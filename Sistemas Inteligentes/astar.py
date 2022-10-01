# OPEN //the set of nodes to be evaluated
# CLOSED //the set of nodes already evaluated
# add the start node to OPEN
 
# loop
#         current = node in OPEN with the lowest f_cost
#         remove current from OPEN
#         add current to CLOSED
 
#         if current is the target node //path has been found
#                 return
 
#         foreach neighbour of the current node
#                 if neighbour is not traversable or neighbour is in CLOSED
#                         skip to the next neighbour
 
#                 if new path to neighbour is shorter OR neighbour is not in OPEN
#                         set f_cost of neighbour
#                         set parent of neighbour to current
#                         if neighbour is not in OPEN
#                                 add neighbour to OPEN


class Spot:
    def __init__(self, row, col, state):
        self.row = row
        self.col = col
        self.state = state
        self.gcost = None
        self.hcost = None
        self.fcost = None
        self.parent = None
        if state == 1:
            self.isStart = True
        if state == 2:
            self.isEnd = True
    
    def getState(self):
        return self.state
    def setState(self, state):
        self.state = state
        
    def getH(self):
        return self.hcost
    def setH(self,hcost):
        self.hcost = hcost
        
    def getG(self):
        return self.gcost
    def setG(self,gcost):
        self.gcost = gcost
        
    def getf(self):
        return self.hcost
    def setf(self,fcost):
        self.fcost = fcost
    def calcF(self):
        self.fcost = self.hcost + self.gcost
        
    def getParent(self):
        return self.parent
    def setParent(self,parent):
        self.parent = parent
        
    def ret
        
def makegrid(base, rows, cols):
    grid = []
    
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(Spot(i,j,base[i][j]))
    return grid

def astar(grid, start, end):
    op = [start]
    cl = []
    start.hcost = abs(start.row - end.row) + abs(start.col - end.col)
    start.gcost = 0
    start.calcF()
    
    while len(op) > 0:
        p = 0
        current = op[0]
        for i in range(1, len(op)):
            if op[i].fcost < current.fcost or op[i].fcost == current.fcost and op[i].hcost < current.hcost:
                current = op[i]
                p = i
        op.pop(p)
        cl.append(current)
        
        if current == end:
            break
        
        checkX = (current.row - 1) >= 0
        checkY = (current.col - 1) >= 0
        
        for i in range(-1,2):
            if checkX or i >= 0:
                for j in range(-1,2):
                    if checkY or j >= 0:
                        if i != 0 and j != 0 and grid[i][j].state != 3 or grid[i][j] not in cl:
                            tempG = current.gcost + 
                    
        
    return

def main():
    base = [
        [1,3,0,0],
        [0,3,0,0],
        [0,0,3,0],
        [3,3,0,2]
    ]
    rows = len(base)
    cols = len(base[0])
    grid = makegrid(base, rows, cols)
    arr = []
    for i in range(rows):
        arr.append([])
        for j in range(cols):
            arr[i].append(grid[i][j].state)
    for i in range(rows):
        print(arr[i])

if __name__ == "__main__":
    main()
