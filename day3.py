import math
import collections
import copy
from operator import add, sub


class untangle:

    start = 0
    x_counter = 0
    pointerrow = start
    pointercolumn = start
    matrix = collections.defaultdict(lambda: collections.defaultdict(lambda: '.'))
    matrix[pointerrow][pointercolumn] = 'O'
   

    def draw_a_direction(self, direction, which_wire):
        horizontal = '-' if which_wire == 2 else '_'
        vertical = '|' if which_wire == 2 else '^'
        maths = add if direction[0] in ('R', 'D') else sub
        horizontal2 = '_' if which_wire == 2 else '-'
        vertical2 = '^' if which_wire == 2 else '|'
        distance = int(direction[1:])

        for _ in range(distance):
            if direction[0] in ('R', 'L'):
                untangle.pointercolumn = maths(untangle.pointercolumn, 1)
                slot = untangle.matrix[untangle.pointerrow][untangle.pointercolumn]
                untangle.matrix[untangle.pointerrow][untangle.pointercolumn] = 'X' if slot == vertical else horizontal2
            else:
                untangle.pointerrow = maths(untangle.pointerrow, 1)
                slot = untangle.matrix[untangle.pointerrow][untangle.pointercolumn]
                untangle.matrix[untangle.pointerrow][untangle.pointercolumn] = 'X' if slot == horizontal else vertical2
            

    def find_closest_x(self):
        current_shortest_distance = math.inf

        for index_of_line, line in untangle.matrix.items():
            for index_of_slot, slot in line.items(): 
                if slot == 'X':
                    untangle.x_counter += 1
                    manhattan_distance = (abs(index_of_slot)) + (abs(index_of_line))
                    if manhattan_distance < current_shortest_distance:
                        current_shortest_distance = manhattan_distance
        print(current_shortest_distance)



    def wiretracer(self):
        with open("day3input1.txt") as directionfile:
            for wire in range(1, 3):
                line_of_directions = directionfile.readline()
                line_of_directions = line_of_directions.split(',')
                for direction in line_of_directions:
                    self.draw_a_direction(direction, wire)
                # resetting the pointer to starting location
                untangle.pointercolumn = untangle.start
                untangle.pointerrow = untangle.start
        self.find_closest_x()



untangle().wiretracer()
