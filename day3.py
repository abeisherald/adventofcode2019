import math
import collections
import copy
from operator import add, sub


class untangle:

    start = 0
    x_counter = 0
    pointerrow_wire_1 = start
    pointercolumn_wire_1 = start
    matrix = collections.defaultdict(lambda: collections.defaultdict(lambda: '.'))
    matrix[pointerrow_wire_1][pointercolumn_wire_1] = 'O'
   

    def draw_a_direction(self, direction, which_wire):
        horizontal = '-' if which_wire == 2 else '_'
        vertical = '|' if which_wire == 2 else '^'
        maths = add if direction[0] in ('R', 'D') else sub
        horizontal2 = '_' if which_wire == 2 else '-'
        vertical2 = '^' if which_wire == 2 else '|'
        distance = int(direction[1:])

        for _ in range(distance):
            if direction[0] in ('R', 'L'):
                untangle.pointercolumn_wire_1 = maths(untangle.pointercolumn_wire_1, 1)
                slot = untangle.matrix[untangle.pointerrow_wire_1][untangle.pointercolumn_wire_1]
                untangle.matrix[untangle.pointerrow_wire_1][untangle.pointercolumn_wire_1] = 'X' if slot == vertical else horizontal2
            else:
                untangle.pointerrow_wire_1 = maths(untangle.pointerrow_wire_1, 1)
                slot = untangle.matrix[untangle.pointerrow_wire_1][untangle.pointercolumn_wire_1]
                untangle.matrix[untangle.pointerrow_wire_1][untangle.pointercolumn_wire_1] = 'X' if slot == horizontal else vertical2
            

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

    
    def find_shortest_x_distance(self):
        pointerrow_wire_1 = 0
        pointercolumn_wire_1 = 0
        pointerrow_wire_2 = 0
        pointercolumn_wire_2 = 0
        current_shortest_distance_to_x = math.inf
        matrix = copy.copy(untangle.matrix)
        x_counter = untangle.x_counter
        distance_counter_wire_1 = 0
        distance_counter_wire_2 = 0
        
        while x_counter > 0:
            for wire in range(2):
                while wire == 0:
                    if matrix[pointerrow_wire_1][pointercolumn_wire_1 + 1] == '-':
                        distance_counter_wire_1 += 1
                        pointercolumn_wire_1 += 1
                        matrix[pointerrow_wire_1][pointercolumn_wire_1] = '.'
                    elif matrix[pointerrow_wire_1][pointercolumn_wire_1 - 1] == '-':
                        distance_counter_wire_1 += 1
                        pointercolumn_wire_1 -= 1
                        matrix[pointerrow_wire_1][pointercolumn_wire_1] = '.'
                    elif matrix[pointerrow_wire_1 + 1][pointercolumn_wire_1] == '|':
                        distance_counter_wire_1 += 1
                        pointerrow_wire_1 += 1
                        matrix[pointerrow_wire_1][pointercolumn_wire_1] = '.'
                    elif matrix[pointerrow_wire_1 - 1][pointercolumn_wire_1] == '|':
                        distance_counter_wire_1 += 1
                        pointerrow_wire_1 -= 1
                        matrix[pointerrow_wire_1][pointercolumn_wire_1] = '.'
                    elif matrix[pointerrow_wire_1][pointercolumn_wire_1 + 1] == 'X':
                        distance_counter_wire_1 += 1
                        x_counter -= 1
                        matrix[pointerrow_wire_1][pointercolumn_wire_1] = '.'
                        break
                    elif matrix[pointerrow_wire_1][pointercolumn_wire_1 - 1] == 'X':
                        distance_counter_wire_1 += 1
                        x_counter -= 1
                        matrix[pointerrow_wire_1][pointercolumn_wire_1] = '.'
                        break
                    elif matrix[pointerrow_wire_1 + 1][pointercolumn_wire_1] == 'X':
                        distance_counter_wire_1 += 1
                        x_counter -= 1
                        matrix[pointerrow_wire_1][pointercolumn_wire_1] = '.'
                        break
                    elif matrix[pointerrow_wire_1 - 1][pointercolumn_wire_1] == 'X':
                        distance_counter_wire_1 += 1
                        x_counter -= 1
                        matrix[pointerrow_wire_1][pointercolumn_wire_1] = '.'
                        break
                    
                while wire == 1:
                    if matrix[pointerrow_wire_2][pointercolumn_wire_2 + 1] == '_':
                        distance_counter_wire_2 += 1
                        pointercolumn_wire_2 += 1
                        matrix[pointerrow_wire_2][pointercolumn_wire_2] = '.'
                    elif matrix[pointerrow_wire_2][pointercolumn_wire_2 - 1] == '_':
                        distance_counter_wire_2 += 1
                        pointercolumn_wire_2 -= 1
                        matrix[pointerrow_wire_2][pointercolumn_wire_2] = '.'
                    elif matrix[pointerrow_wire_2 + 1][pointercolumn_wire_2] == '^':
                        distance_counter_wire_2 += 1
                        pointerrow_wire_2 += 1
                        matrix[pointerrow_wire_2][pointercolumn_wire_2] = '.'
                    elif matrix[pointerrow_wire_2 - 1][pointercolumn_wire_2] == '^':
                        distance_counter_wire_2 += 1
                        pointerrow_wire_2 -= 1
                        matrix[pointerrow_wire_2][pointercolumn_wire_2] = '.'
                    elif matrix[pointerrow_wire_2][pointercolumn_wire_2 + 1] == 'X':
                        distance_counter_wire_2 += 1
                        x_counter -= 1
                        matrix[pointerrow_wire_2][pointercolumn_wire_2] = '.'
                        break
                    elif matrix[pointerrow_wire_2][pointercolumn_wire_2 - 1] == 'X':
                        distance_counter_wire_2 += 1
                        x_counter -= 1
                        matrix[pointerrow_wire_2][pointercolumn_wire_2] = '.'
                        break
                    elif matrix[pointerrow_wire_2 + 1][pointercolumn_wire_2] == 'X':
                        distance_counter_wire_2 += 1
                        x_counter -= 1
                        matrix[pointerrow_wire_2][pointercolumn_wire_2] = '.'
                        break
                    elif matrix[pointerrow_wire_2 - 1][pointercolumn_wire_2] == 'X':
                        distance_counter_wire_2 += 1
                        x_counter -= 1
                        matrix[pointerrow_wire_2][pointercolumn_wire_2] = '.'
                        break
                    
                
            distance_to_x = distance_counter_wire_1 + distance_counter_wire_2
            if distance_to_x < current_shortest_distance_to_x:
                current_shortest_distance_to_x = distance_to_x
        print(current_shortest_distance_to_x)



    def wiretracer(self):
        with open("day3input1.txt") as directionfile:
            for wire in range(1, 3):
                line_of_directions = directionfile.readline()
                line_of_directions = line_of_directions.split(',')
                for direction in line_of_directions:
                    self.draw_a_direction(direction, wire)
                # resetting the pointer to starting location
                untangle.pointercolumn_wire_1 = untangle.start
                untangle.pointerrow_wire_1 = untangle.start
        self.find_closest_x()
        self.find_shortest_x_distance()


untangle().wiretracer()
