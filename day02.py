import os
from typing import List

os.environ["DAY"] = "02"


class Game:
    """blah"""
    def __init__(self, game_number: int, game_str: str):
        # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        self.game_number: int = game_number
        self.subsets: List[dict] = []
        _, subsets = game_str.split(': ')
        # subsets should be:
        # [{'blue':3},{'red':4},...]
        self.load_subsets(subsets)
        self.max_qtys: dict = {
            'red': 12,
            'green': 13,
            'blue': 14
        }

        self.colors = [
            'red',
            'blue',
            'green'
        ]

    @property
    def is_good_game(self):
        good_game: bool = True
        for subset in self.subsets:
            for color, qty in self.max_qtys.items():
                if color in subset and subset[color] > qty:
                    good_game = False
        return good_game

    def load_subsets(self, subsets: str):
        # 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
        subsets: List[str] = subsets.split('; ')
        subset_list: List = []
        for subset in subsets:
            # subset = 3 blue, 4 red
            dice_picked = subset.split(', ')
            dice_dict: dict = {}
            for dice in dice_picked:
                qty, color = dice.split(' ')
                dice_dict[color] = int(qty)
            subset_list.append(dice_dict)
        self.subsets = subset_list

    def max_value_for_color(self, color: str) -> int:
        max_color: int = 0
        for subset in self.subsets:
            if color in subset:
                max_color = max(max_color, subset[color])
        print(f"high for color: {color} is: {max_color}")
        return max_color

    def power_of_max_cubes(self):
        power: int = 1
        for color in self.colors:
            power *= self.max_value_for_color(color)
        return power


def sum_of_possible_ids(input_list):
    games: List[Game] = []
    for index, line in enumerate(input_list):
        games.append(Game(index+1, line))

    good_games: int = 0
    for game in games:
        if game.is_good_game:
            good_games += game.game_number
    return good_games


def power_of_cubes(input_list):
    games: List[Game] = []
    for index, line in enumerate(input_list):
        games.append(Game(index+1, line))

    sum_of_powers: int = 0
    for game in games:
        sum_of_powers += game.power_of_max_cubes()
    return sum_of_powers
