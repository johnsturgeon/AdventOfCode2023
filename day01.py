import os
import sys
from typing import List, Optional

os.environ["DAY"] = "01"


def sum_of_calibration(input_list: List, do_replacement: bool = False) -> int:
    total: int = 0
    for line in input_list:
        if do_replacement:
            line = replace_with_digit(line)
        digits = get_digit(line) + get_digit(line, True)
        total += int(digits)
    return total


def get_digit(input_line: str, last: bool = False) -> str:
    return_letter: str = ' '
    for letter in input_line:
        if letter.isdigit():
            if not last:
                return letter
            return_letter = letter
    return return_letter


def replace_with_digit(input_line) -> str:
    return_line: str = input_line
    numbers = [
        'one',
        'two',
        'three',
        'four',
        'five',
        'six',
        'seven',
        'eight',
        'nine'
    ]
    # create number position dict
    number_positions = {}
    index: int = 1
    for number in numbers:
        number_positions.update({number: str(index)})
        index += 1

    # Replace earliest occurrence
    min_str_position: int = sys.maxsize
    min_str: str = ""
    min_repl_str: str = ""
    for string, _ in number_positions.items():
        # {'one': '1'} etc...
        position = input_line.find(string)
        if position != -1 and position < min_str_position:
            min_str_position = position
            min_str = string
            min_repl_str = number_positions[min_str]

    min_num_position: int = sys.maxsize
    min_num: str = ""
    for _, num in number_positions.items():
        # {'one': '1'} etc...
        position = input_line.find(num)
        if position != -1 and position < min_num_position:
            min_num_position = position

    if min_str_position < min_num_position:
        return_line = return_line.replace(min_str, min_repl_str)

    # Replace latest occurrence
    max_str_position: int = -1
    max_str: str = ""
    max_repl_str: str = ""
    for string, _ in number_positions.items():
        # {'one': '1'} etc...
        position = input_line.rfind(string)
        if position != -1 and position > max_str_position:
            max_str_position = position
            max_str = string
            max_repl_str = number_positions[max_str]

    max_num_position: int = -1
    max_num: str = ""
    for _, num in number_positions.items():
        # {'one': '1'} etc...
        position = input_line.rfind(num)
        if position != -1 and position > max_num_position:
            max_num_position = position

    if max_str_position > max_num_position:
        return_line = return_line.replace(max_str, max_repl_str)

    return return_line
