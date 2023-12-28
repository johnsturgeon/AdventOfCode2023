import os
from typing import List
from dataclasses import dataclass

os.environ["DAY"] = "03"



@dataclass
class Gear:
    x_pos: int
    row: int

@dataclass
class PartNumber:
    part_number: int
    start: int
    end: int
    row: int

    def is_gear_adjacent(self, gear: Gear) -> bool:
        if gear.row > self.row + 1 or gear.row < self.row -1:
            return False
        if gear.x_pos > self.end + 1 or gear.x_pos < self.start - 1:
            return False
        return True


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


# Part 2 methods
def create_part_list(input_list) -> List[PartNumber]:
    part_number_list: List[PartNumber] = []
    for row, line in enumerate(input_list):
        line_position: int = 0
        while True:
            number, start, end = find_number_in_line(line, line_position)
            if not number:
                break
            prev_line = previous_row_has_symbol_near_part(input_list, row, start, end)
            next_line = next_row_has_symbol_near_part(input_list, row, start, end)
            current_line = current_row_has_symbol_near_part(input_list, row, start, end)
            if prev_line or next_line or current_line:
                part_number_list.append(PartNumber(
                    start=start,
                    end=end,
                    part_number=number,
                    row=row
                ))
            line_position = end + 1
    return part_number_list


def create_gear_list(input_list) -> List[Gear]:
    gear_list: List[Gear] = []
    for row_number, row in enumerate(input_list):
        for x_pos, char in enumerate(row):
            if char == '*':
                gear_list.append(Gear(x_pos=x_pos, row=row_number))
    return gear_list


# Starting point for part 2
def sum_of_gear_products(input_list):
    part_list: List[PartNumber] = create_part_list(input_list)
    gear_list: List[Gear] = create_gear_list(input_list)
    sum_of_products: int = 0
    for gear in gear_list:
        adjacent_parts: List[int] = []
        for part in part_list:
            if part.is_gear_adjacent(gear):
                adjacent_parts.append(part.part_number)
        if len(adjacent_parts) == 2:
            sum_of_products += adjacent_parts[0] * adjacent_parts[1]
    return sum_of_products


def sum_of_part_numbers(input_list):
    part_number_sum: int = 0
    for row, line in enumerate(input_list):
        line_position: int = 0
        while True:
            number, start, end = find_number_in_line(line, line_position)
            if not number:
                break
            prev_line = previous_row_has_symbol_near_part(input_list, row, start, end)
            next_line = next_row_has_symbol_near_part(input_list, row, start, end)
            current_line = current_row_has_symbol_near_part(input_list, row, start, end)
            if prev_line or next_line or current_line:
                part_number_sum += number
            line_position = end + 1

    return part_number_sum


