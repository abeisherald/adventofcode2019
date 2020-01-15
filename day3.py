import copy

example = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
example2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

# example = ['R8', 'U5', 'L5', 'D3']
# example2 = ['U7', 'R6', 'D4', 'L4']

class untangle:

    start = 500
    pointerlevel = copy.copy(start)
    pointercolumn = copy.copy(start)
    matrix = {}
    pointerstart = False

    for level in range(1000): 
        matrix[level] = ['.'] * 1000

    while not pointerstart:
        matrix[pointerlevel][pointercolumn] = 'O'
        pointerstart = True


    def drawadirection(self, adirection):
            if adirection[0] == 'R':
                distance = int(adirection[1:3])
                for x in range(distance):
                    untangle.pointercolumn += 1
                    if untangle.matrix[untangle.pointerlevel][untangle.pointercolumn] == '|':
                        untangle.matrix[untangle.pointerlevel][untangle.pointercolumn] = 'X'
                    else:
                        untangle.matrix[untangle.pointerlevel][untangle.pointercolumn] = '-'
            elif adirection[0] == 'L':
                distance = int(adirection[1:3])
                for x in range(distance):
                    untangle.pointercolumn -= 1
                    if untangle.matrix[untangle.pointerlevel][untangle.pointercolumn] == '|':
                        untangle.matrix[untangle.pointerlevel][untangle.pointercolumn] = 'X'
                    else:
                        untangle.matrix[untangle.pointerlevel][untangle.pointercolumn] = '-'
            elif adirection[0] == 'U':
                distance = int(adirection[1:3])
                for x in range(distance):
                    untangle.pointerlevel -= 1
                    if untangle.matrix[untangle.pointerlevel][untangle.pointercolumn] == '-':
                        untangle.matrix[untangle.pointerlevel][untangle.pointercolumn] = 'X'
                    else:
                        untangle.matrix[untangle.pointerlevel][untangle.pointercolumn] = '|'
            elif adirection[0] == 'D':
                distance = int(adirection[1:3])
                for x in range(distance):
                    untangle.pointerlevel += 1
                    if untangle.matrix[untangle.pointerlevel][untangle.pointercolumn] == '-':
                        untangle.matrix[untangle.pointerlevel][untangle.pointercolumn] = 'X'
                    else:
                        untangle.matrix[untangle.pointerlevel][untangle.pointercolumn] = '|'


    def findclosestx(self):
        start = untangle.start
        currentshortestdistance = 1000

        for indexofline, line in enumerate(untangle.matrix.values()):
            for indexofslot, slot in enumerate(line): 
                if slot == 'X':
                    manhattandistance = (abs(indexofslot - start)) + (abs(indexofline - start))
                    if manhattandistance < currentshortestdistance:
                        currentshortestdistance = manhattandistance
        print(currentshortestdistance)

    
    def wiretracer(self, listofdirections1, listofdirections2):
        #start at 1000,1000 make a point

        for direction in listofdirections1:
            self.drawadirection(direction)
        untangle.pointercolumn = copy.copy(untangle.start)
        untangle.pointerlevel = copy.copy(untangle.start)
        for direction in listofdirections2:
            self.drawadirection(direction)
        self.findclosestx()


        # for line in list(untangle.matrix.values()):
        #     print(line)


untangle().wiretracer(example, example2)
