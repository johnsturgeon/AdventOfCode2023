import day04
from common_fixtures import sample_list, real_list, sample_list_p2, real_list_p2


def test_total_card_value_sample(sample_list):
    assert day04.get_card_point_value(sample_list) == 30


def test_total_card_value(real_list):
    assert day04.get_card_point_value(real_list) == 5921508
