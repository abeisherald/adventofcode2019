import math
import collections
from operator import add, sub


class untangle:

    start = 5000
    pointerlevel = start
    pointercolumn = start
    matrix = collections.defaultdict(lambda: collections.defaultdict(lambda: '.'))
    matrix[pointerlevel][pointercolumn] = 'O'
   

    def drawadirection(self, direction, which_wire):
        x = '-' if which_wire == 2 else '_'
        x2 = '|' if which_wire == 2 else '^'
        x3 = add if direction[0] in ('R', 'D') else sub
        x5 = '_' if which_wire == 2 else '-'
        x6 = '^' if which_wire == 2 else '|'
        distance = int(direction[1:])


        for _ in range(distance):
            if direction[0] in ('R', 'L'):
                untangle.pointercolumn = x3(untangle.pointercolumn, 1)
                slot = untangle.matrix[untangle.pointerlevel][untangle.pointercolumn]
                untangle.matrix[untangle.pointerlevel][untangle.pointercolumn] = 'X' if slot == x2 else x5
            else:
                untangle.pointerlevel = x3(untangle.pointerlevel, 1)
                slot = untangle.matrix[untangle.pointerlevel][untangle.pointercolumn]
                untangle.matrix[untangle.pointerlevel][untangle.pointercolumn] = 'X' if slot == x else x6
            

    def findclosestx(self):
        start = untangle.start
        currentshortestdistance = math.inf

        for indexofline, line in untangle.matrix.items():
            for indexofslot, slot in line.items(): 
                if slot == 'X':
                    manhattandistance = (abs(indexofslot - start)) + (abs(indexofline - start))
                    if manhattandistance < currentshortestdistance:
                        currentshortestdistance = manhattandistance
        print(currentshortestdistance)

    
    def wiretracer(self):
        with open("day3input1.txt") as directionfile:
            for wire in range(1, 3):
                lineofdirections = directionfile.readline()
                lineofdirections = lineofdirections.split(',')
                for direction in lineofdirections:
                    self.drawadirection(direction, wire)
                # resetting the pointer to starting location
                untangle.pointercolumn = untangle.start
                untangle.pointerlevel = untangle.start
        self.findclosestx()


untangle().wiretracer()
