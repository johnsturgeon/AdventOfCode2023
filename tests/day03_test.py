import day03
import os
from common_fixtures import sample_list, real_list, sample_list_p2, real_list_p2


def test_sum_of_parts_sample(sample_list):
    assert day03.sum_of_part_numbers(sample_list) == 4361


def test_sum_of_parts(real_list):
    assert day03.sum_of_part_numbers(real_list) == 539713


def test_sum_of_gear_products_sample(sample_list):
    assert day03.sum_of_gear_products(sample_list) == 467835


def test_sum_of_gear_products(real_list):
    assert day03.sum_of_gear_products(real_list) == 84159075