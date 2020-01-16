import copy

line1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33', 'U53', 'R51']
line2 = ['U98','R91','D20','R16','D67','R40','U7','R15', 'U6', 'R7']

# example = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# example2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

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
            distance = int(adirection[1:])
            for _ in range(distance):
                untangle.pointercolumn += 1
                slot = untangle.matrix[untangle.pointerlevel][untangle.pointercolumn]
                if slot == '|':
                    untangle.matrix[untangle.pointerlevel][untangle.pointercolumn]= 'X'
                else:
                    untangle.matrix[untangle.pointerlevel][untangle.pointercolumn]= '-'
        elif adirection[0] == 'L':
            distance = int(adirection[1:])
            for _ in range(distance):
                untangle.pointercolumn -= 1
                slot = untangle.matrix[untangle.pointerlevel][untangle.pointercolumn]
                if slot == '|':
                    untangle.matrix[untangle.pointerlevel][untangle.pointercolumn] = 'X'
                else:
                    untangle.matrix[untangle.pointerlevel][untangle.pointercolumn] = '-'
        elif adirection[0] == 'U':
            distance = int(adirection[1:])
            for _ in range(distance):
                untangle.pointerlevel -= 1
                slot = untangle.matrix[untangle.pointerlevel][untangle.pointercolumn]
                if slot == '-':
                    untangle.matrix[untangle.pointerlevel][untangle.pointercolumn] = 'X'
                else:
                    untangle.matrix[untangle.pointerlevel][untangle.pointercolumn] = '|'
        elif adirection[0] == 'D':
            distance = int(adirection[1:])
            for _ in range(distance):
                untangle.pointerlevel += 1
                slot = untangle.matrix[untangle.pointerlevel][untangle.pointercolumn]
                if slot == '-':
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

    
    def wiretracer(self):
        with open("day3input.txt") as directionfile:
            for _ in range(2):
                lineofdirections = directionfile.readline()
                lineofdirections = lineofdirections.split(',')
                for direction in lineofdirections:
                    self.drawadirection(direction)
                # resetting the pointer to starting location
                untangle.pointercolumn = copy.copy(untangle.start)
                untangle.pointerlevel = copy.copy(untangle.start)
        self.findclosestx()


untangle().wiretracer()
