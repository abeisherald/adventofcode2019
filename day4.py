import copy

puzzle_input_range_start = 147981
puzzle_input_range_end = 691423


def secret_cracker(input_range_start, input_range_end):
    valid_password_counter = 0


    for number in range(input_range_start, input_range_end):
        digits_increase = False
        current_digit = 0
        adjacency_counter = 0
        number = list(str(number))
        number = iter(number)
        saved_number = copy.copy(number)
        for digit in number:
            if digit == next(number):
                adjacency_counter += 1
        if adjacency_counter >= 1:
            for digit in saved_number:
                digit = int(digit)
                if digit >= current_digit:
                    current_digit = digit
                    digits_increase = True
                else:
                    digits_increase = False
                    break
        if digits_increase:
            valid_password_counter += 1

    print(f'The number of different passwords within the given range is {valid_password_counter}')


secret_cracker(puzzle_input_range_start, puzzle_input_range_end)
