# 1 = +, 2 = *, 99 = exit

intcodeprog = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,9,19,23,1,13,23,27,1,5,27,31,2,31,6,35,1,35,5,39,1,9,39,43,1,43,5,47,1,47,5,51,2,10,51,55,1,5,55,59,1,59,5,63,2,63,9,67,1,67,5,71,2,9,71,75,1,75,5,79,1,10,79,83,1,83,10,87,1,10,87,91,1,6,91,95,2,95,6,99,2,99,9,103,1,103,6,107,1,13,107,111,1,13,111,115,2,115,9,119,1,119,6,123,2,9,123,127,1,127,5,131,1,131,5,135,1,135,5,139,2,10,139,143,2,143,10,147,1,147,5,151,1,151,2,155,1,155,13,0,99,2,14,0,0]
#intcodeprog = [1, 1, 1, 4, 99, 5, 6, 0, 99]


def compumagic(intprogram):
    #intprogram2 = [x for x in intprogram[::4]]
    # for index, opcode in enumerate(intprogram):
    #     if opcode in (1, 2):
    #         inputindex1 = intprogram[(index) + 1]
    #         inputindex2 = intprogram[(index) + 2]
    #         outputindex = intprogram[(index) + 3]
    #         if opcode == 1:
    #             intprogram[outputindex] = intprogram[inputindex1] + intprogram[inputindex2]
    #         else:
    #             intprogram[outputindex] = intprogram[inputindex1] * intprogram[inputindex2]
    #     else:
    #         print(intprogram)
    #         break
    pointer = 0
    while True:

        if intprogram[pointer] != 99:
            if intprogram[pointer] in (1, 2):
                inputindex1 = intprogram[pointer + 1]
                inputindex2 = intprogram[pointer + 2]
                outputindex = intprogram[pointer + 3]
                if intprogram[pointer] == 1:
                    intprogram[outputindex] = intprogram[inputindex1] + \
                        intprogram[inputindex2]
                    pointer += 4
                else:
                    intprogram[outputindex] = intprogram[inputindex1] * \
                        intprogram[inputindex2]
                    pointer += 4
        else:
            print(intprogram)
            break


compumagic(intcodeprog)
