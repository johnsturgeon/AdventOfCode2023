from __future__ import annotations
import os
import sys
from typing import List, Optional, Tuple
import math
os.environ["DAY"] = "06"


def get_distance_time_arrays(input_list) -> Tuple[List[int], List[int]]:
    time_str = input_list[0].split()
    distance_str = input_list[1].split()
    time_ints = []
    distance_ints = []
    for time in time_str:
        if time.isnumeric():
            time_ints.append(int(time))
    for distance in distance_str:
        if distance.isnumeric():
            distance_ints.append(int(distance))
    return time_ints, distance_ints


def get_concat_time_distance(input_list) -> Tuple[int, int]:
    time_str = input_list[0].split()
    distance_str = input_list[1].split()
    cat_time_str: str = ""
    cat_distance_str: str = ""
    for time in time_str:
        if time.isnumeric():
            cat_time_str += time
    for distance in distance_str:
        if distance.isnumeric():
            cat_distance_str += distance
    return int(cat_time_str), int(cat_distance_str)


def can_win(time, distance, push_time) -> bool:
    if push_time == 0:
        return False
    remaining_time = time - push_time # 6 seconds
    travel_dist: int = push_time * remaining_time
    if travel_dist > distance:
        return True
    return False


def part1(input_list):
    distances: List[int]
    record_times, distances = get_distance_time_arrays(input_list)

    # iterate over each race
    can_win_race_total: List[int] = []
    for i,_ in enumerate(record_times):
        race_total_wins: int = 0
        for push_time in range(1, distances[i]):
            if can_win(push_time=push_time, distance=distances[i], time=record_times[i]):
                race_total_wins += 1
        can_win_race_total.append(race_total_wins)
    return math.prod(can_win_race_total)


def part2(input_list):
    record_time, record_distance = get_concat_time_distance(input_list=input_list)
    race_total_wins: int = 0
    for push_time in range(1, record_time):
        if can_win(push_time=push_time, distance=record_distance, time=record_time):
            race_total_wins += 1
    return race_total_wins
