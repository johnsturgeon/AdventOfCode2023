from typing import List
import pytest
import os

day = os.environ["DAY"]


def get_list(filename):
    real_list = []
    with open(filename, 'r') as file_handle:
        for line in file_handle:
            real_list.append(line.strip('\n'))
    return real_list


@pytest.fixture
def sample_list() -> List:
    return get_list(f"data/day{day}_sample.txt")


@pytest.fixture
def real_list() -> List:
    return get_list(f"data/day{day}.txt")


@pytest.fixture
def sample_list_p2() -> List:
    return get_list(f"data/day{day}_p2_sample.txt")


@pytest.fixture
def real_list_p2() -> List:
    return get_list(f"data/day{day}_p2.txt")

