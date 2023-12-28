import day05
from common_fixtures import sample_list, real_list, sample_list_p2, real_list_p2


def test_part1_sample(sample_list):
    assert day05.part1(sample_list) == 35


def test_part1(real_list):
    assert day05.part1(real_list) == 51580674


def test_part2_sample(sample_list):
    assert day05.part2(sample_list) == 46


def test_part2(real_list):
    assert day05.part2(real_list) == 99751240
