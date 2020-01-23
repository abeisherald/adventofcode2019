from operator import add, mul, lt, eq, ne





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

        opcode = instruction[4:5]
        parameter_1 = instruction[2:3]
        parameter_2 = instruction[1:2]
        inputindex1 = intprogram[pointer + 1]
        inputindex2 = intprogram[pointer + 2]
        outputindex = intprogram[pointer + 3]
        
        # 0=position mode, 1=immediate mode
        if opcode in ('1', '2', '5', '6', '7', '8'):
            parameter_1_mode = intprogram[inputindex1] if parameter_1 == '0' else inputindex1
            parameter_1_mode_index2 = intprogram[inputindex2] if parameter_1 == '0' else inputindex2
            parameter_2_mode = intprogram[inputindex2] if parameter_2 == '0' else inputindex2
            parameter_2_mode_index1 = intprogram[inputindex1] if parameter_2 == '0' else inputindex1

        
        if opcode in ('1', '2'):
            operator = add if opcode == '1' else mul
            intprogram[outputindex] = operator(parameter_1_mode, parameter_2_mode)
            pointer += 4
        elif opcode == '3':
            input_value = int(input(f'Provide a single integer: '))
            outputindex = intprogram[pointer + 1]
            intprogram[outputindex] = input_value
            pointer += 2
        elif opcode == '4':
            opcode_4_output = intprogram[pointer + 1] if parameter_1 == '0' else (pointer + 1)
            output = intprogram[opcode_4_output]
            print(f'The output is {output}.')
            pointer += 2
        elif opcode in ('5', '6'):
            operator = ne if opcode == '5' else eq
            pointer = parameter_1_mode_index2 if operator(parameter_1, '0') else pointer
            x = 0 if operator(parameter_1, '0') else 3
            pointer += x
        elif opcode in ('7', '8'):
            operator = lt if opcode == '7' else eq
            x = 1 if operator(parameter_1_mode, parameter_2_mode) else 0
            intprogram[outputindex] = x
            pointer += 4
    else:
        print(f'Program complete')

compumagic()