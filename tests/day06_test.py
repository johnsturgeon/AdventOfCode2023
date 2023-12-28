import day06
from common_fixtures import sample_list, real_list, sample_list_p2, real_list_p2


def test_part1_sample(sample_list):
    assert day06.part1(sample_list) == 288


def test_part1(real_list):
    assert day06.part1(real_list) == 588588


def test_part2_sample(sample_list):
    assert day06.part2(sample_list) == 71503


def test_part2(real_list):
    assert day06.part2(real_list) == 34655848
