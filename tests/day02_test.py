import day02
import os
from common_fixtures import sample_list, real_list, sample_list_p2, real_list_p2


def test_sum_of_possible_ids_sample(sample_list):
    assert day02.sum_of_possible_ids(sample_list) == 8


def test_sum_of_possible_ids(real_list):
    assert day02.sum_of_possible_ids(real_list) == 2076


def test_power_of_cubes_sample(sample_list):
    assert day02.power_of_cubes(sample_list) == 2286


def test_power_of_cubes(real_list):
    assert day02.power_of_cubes(real_list) == 2286
