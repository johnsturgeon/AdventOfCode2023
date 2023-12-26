import os
from typing import List

os.environ["DAY"] = "03"


def previous_row_has_symbol_near_part(input_list, current_row_index, start, end) -> bool:
    if current_row_index == 0:
        return False
    row = input_list[current_row_index - 1]
    for position, char in enumerate(row):
        if char.isdigit() or char == '.':
            continue
        if start-1 <= position <= end+1:
            return True
    return False


def next_row_has_symbol_near_part(input_list, current_row_index, start, end) -> bool:
    if current_row_index >= len(input_list) - 1:
        return False
    row = input_list[current_row_index + 1]
    for position, char in enumerate(row):
        if char.isdigit() or char == '.':
            continue
        if start-1 <= position <= end+1:
            return True
    return False


def current_row_has_symbol_near_part(input_list, current_row_index, start, end) -> bool:
    line = input_list[current_row_index]
    found_symbol: bool = False
    if start > 0 and line[start-1] != '.':
        return True
    if end < (len(line) - 1) and line[end+1] != '.':
        return True
    return False


def find_number_in_line(line, start_index):
    found_digits = ""
    found_positions = []
    for i in range(start_index, len(line)):
        if line[i].isdigit():
            found_positions.append(i)
            found_digits += line[i]
        elif len(found_digits):
            break
    if not found_digits:
        return 0, 0, 0
    else:
        number = int(found_digits)
        return number, found_positions[0], found_positions[-1]


def sum_of_part_numbers(input_list):
    part_number_sum: int = 0
    for row, line in enumerate(input_list):
        line_position: int = 0
        while True:
            number, start, end = find_number_in_line(line, line_position)
            if not number:
                break
            print(number)
            prev_line = previous_row_has_symbol_near_part(input_list, row, start, end)
            next_line = next_row_has_symbol_near_part(input_list, row, start, end)
            current_line = current_row_has_symbol_near_part(input_list, row, start, end)
            if prev_line or next_line or current_line:
                part_number_sum += number
            else:
                print("Bad Part")
            line_position = end + 1
    return part_number_sum


