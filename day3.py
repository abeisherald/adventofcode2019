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

    
    def find_shortest_x_distance(self):

        wire_is_incomplete = True
        x_counter = untangle.x_counter
        distance_keeper = {k:[] for k in range(x_counter)}
        current_shortest_distance_to_x = math.inf
       
        for which_wire in range(1, 3):
            while wire_is_incomplete:
                horizontal2 = '_' if which_wire == 2 else '-'
                vertical2 = '^' if which_wire == 2 else '|'
                pointercolumn_wire_1 = 0
                pointercolumn_wire_2 = 0
                pointerrow_wire_1 = 0
                pointerrow_wire_2 = 0
                pointerrow = pointerrow_wire_2 if which_wire == 2 else pointerrow_wire_1
                pointercolumn = pointercolumn_wire_2 if which_wire == 2 else pointercolumn_wire_1
                distance_counter_wire_1 = 0
                distance_counter_wire_2 = 0
                distance_counter = distance_counter_wire_2 if which_wire == 2 else distance_counter_wire_1
                matrix = copy.copy(untangle.matrix)
                x_counter = untangle.x_counter
                right = False
                left = False
                up = False
                down = False
                

                
                
                if matrix[pointerrow][pointercolumn + 1] == horizontal2:
                    right = True
                elif matrix[pointerrow][pointercolumn - 1] == horizontal2:
                    right = True
                elif matrix[pointerrow + 1][pointercolumn] == vertical2:
                    down = True
                elif matrix[pointerrow - 1][pointercolumn] == vertical2:
                    up = True
                else:
                    wire_is_incomplete = False
                    break
                
                direction_maths = 1 if right == True or down == True else -1 

                
                while right or left:
                    slot = matrix[pointerrow][pointercolumn + direction_maths]
                    if slot == '.':
                        right = left = False
                    elif slot == horizontal2:
                        pointercolumn += direction_maths
                        matrix[pointerrow][pointercolumn] = '.'
                        distance_counter += 1
                    elif slot[:1] == 'X':
                        pointercolumn += direction_maths
                        matrix[pointerrow][pointercolumn] = 'X' + x_counter
                        distance_counter += 1
                        distance_keeper[x_counter] = distance_keeper[x_counter].append(distance_counter)
                        x_counter -= 1

                while up or down:
                    slot = matrix[pointerrow][pointercolumn + direction_maths]
                    if slot == False:
                        up = down = False
                    elif slot == vertical2:
                        pointerrow += direction_maths
                        matrix[pointerrow][pointercolumn] = '.'
                        distance_counter += 1
                    elif slot[:1] == 'X':
                        pointerrow += direction_maths
                        matrix[pointerrow][pointercolumn] = 'X' + x_counter
                        distance_counter += 1
                        distance_keeper[x_counter] = distance_keeper[x_counter].append(distance_counter)
                        x_counter -= 1
                        
                    
        for x_name, x_distances_from_center in distance_keeper:
            distance_to_x = x_distances_from_center[0] + x_distances_from_center[1]                
            if distance_to_x < current_shortest_distance_to_x:
                current_shortest_distance_to_x = distance_to_x
        print(current_shortest_distance_to_x)



    def wiretracer(self):
        with open("day3input.txt") as directionfile:
            for wire in range(1, 3):
                line_of_directions = directionfile.readline()
                line_of_directions = line_of_directions.split(',')
                for direction in line_of_directions:
                    self.draw_a_direction(direction, wire)
                # resetting the pointer to starting location
                untangle.pointercolumn = untangle.start
                untangle.pointerrow = untangle.start
        self.find_closest_x()
        self.find_shortest_x_distance()


untangle().wiretracer()
