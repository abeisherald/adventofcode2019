example = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
example2 = ['U62','R66','U55','R34','D71','R55','D58','R83']


def wiretracer(listofdirections1, listofdirections2):
    matrix = {}
    
    for level in range(2000): 
            matrix[level] = ['.'] * 2000
    # print(matrix)

    #start at 0,0
    start = True
    pointerrow = 1000
    pointerlevel = 1000
    while start:
        for direction in listofdirections1:
            if direction[0] == 'R':
                distance = int(direction[1:3])
                for x in range(distance):
                    pointerrow += 1
                    matrix[pointerlevel][pointerrow] = '-'
            elif direction[0] == 'L':
                distance = int(direction[1:3])
                for x in range(distance):
                    pointerrow -= 1
                    matrix[pointerlevel][pointerrow] = '-'
            elif direction[0] == 'U':
                distance = int(direction[1:3])
                for x in range(distance):
                    pointerlevel -= 1
                    matrix[pointerlevel][pointerrow] = '|'
            elif direction[0] == 'D':
                distance = int(direction[1:3])
                for x in range(distance):
                    pointerlevel += 1
                    matrix[pointerlevel][pointerrow] = '|'
            else:
                print(f'done wire')
                start = False



wiretracer(example, example2)
