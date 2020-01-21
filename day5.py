from operator import add, mul





def compumagic():
    pointer = 0

    with open('day5input.txt') as program:
        intprogram = program.readline().split(',')
    for index, instruction in enumerate(intprogram):
        intprogram[index] = int(instruction)



    while intprogram[pointer] != 99:
        instruction = intprogram[pointer]
        instruction = str(instruction)
        while len(instruction) < 5:
            instruction = '0' + instruction
        else:
            opcode = instruction[4:5]
            parameter_1 = instruction[2:3]
            parameter_2 = instruction[1:2]

        # 0=position mode, 1=immediate mode
        if opcode in ('1', '2'):
            inputindex1 = intprogram[pointer + 1]
            inputindex2 = intprogram[pointer + 2]
            outputindex = intprogram[pointer + 3]
            parameter_1_input = intprogram[inputindex1] if parameter_1 == '0' else inputindex1
            parameter_2_input = intprogram[inputindex2] if parameter_2 == '0' else inputindex2
            f = add if opcode == '1' else mul
            intprogram[outputindex] = f(parameter_1_input, parameter_2_input)
            pointer += 4
        if opcode == '3':
            input_value = int(input(f'Provide a single integer: '))
            outputindex = intprogram[pointer + 1]
            intprogram[outputindex] = input_value
            pointer += 2
        if opcode == '4':
            opcode_4_output = intprogram[pointer + 1] if parameter_1 == '0' else (pointer + 1)
            output = intprogram[opcode_4_output]
            print(f'The output is {output}.')
            pointer += 2
    else:
        print(f'Program complete')

compumagic()