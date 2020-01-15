# example = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
# example2 = ['U62','R66','U55','R34','D71','R55','D58','R83']

example = ['R8', 'U5', 'L5', 'D3']
example2 = ['U7', 'R6', 'D4', 'L4']

class untangle:

    pointerlevel = 10
    pointerrow = 10
    matrix = {}
    for level in range(20): 
        matrix[level] = ['.'] * 20


    def drawadirection(self, adirection):
            if adirection[0] == 'R':
                distance = int(adirection[1:3])
                for x in range(distance):
                    untangle.pointerrow += 1
                    untangle.matrix[untangle.pointerlevel][untangle.pointerrow] = '-'
            elif adirection[0] == 'L':
                distance = int(adirection[1:3])
                for x in range(distance):
                    untangle.pointerrow -= 1
                    untangle.matrix[untangle.pointerlevel][untangle.pointerrow] = '-'
            elif adirection[0] == 'U':
                distance = int(adirection[1:3])
                for x in range(distance):
                    untangle.pointerlevel -= 1
                    untangle.matrix[untangle.pointerlevel][untangle.pointerrow] = '|'
            elif adirection[0] == 'D':
                distance = int(adirection[1:3])
                for x in range(distance):
                    untangle.pointerlevel += 1
                    untangle.matrix[untangle.pointerlevel][untangle.pointerrow] = '|'


    def wiretracer(self, listofdirections1, listofdirections2):
        #start at 1000,1000 make a point

        for direction in listofdirections1:
            self.drawadirection(direction)
        untangle.pointerrow = 10
        untangle.pointerlevel = 10
        for direction in listofdirections2:
            self.drawadirection(direction)



        for line in untangle.matrix.values():
            for index, slot in enumerate(line):
                try:
                    if slot == '-' and slot[index + 1] == '|':
                        if slot[index + 2] == '-':
                            slot[index + 1] = 'X'
                except:
                    continue  


        for line in list(untangle.matrix.values()):
            print(line)


untangle().wiretracer(example, example2)