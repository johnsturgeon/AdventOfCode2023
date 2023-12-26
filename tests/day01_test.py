import day01
import os
from common_fixtures import sample_list, real_list, sample_list_p2, real_list_p2


def test_sum_of_calibration_sample(sample_list):
    assert day01.sum_of_calibration(sample_list) == 142


def test_sum_of_calibration(real_list):
    assert day01.sum_of_calibration(real_list) == 54159


def test_sum_of_words_sample(sample_list_p2):
    assert day01.sum_of_calibration(sample_list_p2, True) == 281


def test_sum_of_words(real_list):
    assert day01.sum_of_calibration(real_list, True) == 53866