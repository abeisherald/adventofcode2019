from operator import add, sub

program = 3,0,4,0,99

def compumagic(intprogram):
    pointer = 0
    intprogram = list(intprogram)

    # while True:
    #     instruction = intprogram[pointer]
    #     if len(str(instruction)) < 5:
    #         instruction = 0 + instruction
    #     else:
    #         opcode = str(instruction)[3:5]
    #         parameter_1 = str(instruction)[2:3]
    #         parameter_2 = str(instruction)[1:2]
    #         parameter_3 = str(instruction)[0:1]

    while intprogram[pointer] != 99:


        if intprogram[pointer] in (1, 2):
            inputindex1 = intprogram[pointer + 1]
            inputindex2 = intprogram[pointer + 2]
            outputindex = intprogram[pointer + 3]
            f = add if intprogram[pointer] == 1 else mul
            intprogram[outputindex] = f(intprogram[inputindex1], intprogram[inputindex2])
            pointer += 4
        if intprogram[pointer] == 3:
            input_value = int(input(f'Provide a single integer: '))
            outputindex = intprogram[pointer + 1]
            intprogram[outputindex] = input_value
            pointer += 2
        if intprogram[pointer] == 4:
            output = intprogram[intprogram[pointer + 1]]
            print(f'The output is {output}.')
            pointer += 2
    else:
        print(f'Program complete')

compumagic(program)