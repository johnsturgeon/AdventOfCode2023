from __future__ import annotations
import os
import sys
from typing import List, Optional, Tuple
from dataclasses import dataclass

os.environ["DAY"] = "06"


class Source:
    def __init__(self, name=None):
        self.name = name
        self.destination: Optional[Source] = None
        self._mappings = []

    def add_range_map(self, source_begin: int, source_len: int, dest_delta: int):
        range_begin: int = source_begin
        range_end: int = source_begin + source_len
        range_delta: int = dest_delta
        self._mappings.append({
            'begin': range_begin,
            'end': range_end,
            'delta': range_delta
        })

    def _find_mapping(self, location):
        mapped_location: int = location
        for mapping in self._mappings:
            if mapping['begin'] <= location < mapping['end']:
                mapped_location = location + mapping['delta']
        return mapped_location

    def get_mapped_location(self, location) -> int:
        mapped_location: int = self._find_mapping(location)
        if self.destination:
            mapped_location = self.destination.get_mapped_location(mapped_location)
        return mapped_location

    def _find_mapping_ranges(self, r1s: List[range]) -> List[range]:
        mapping_ranges: List[range] = []
        for r1 in r1s:
            if len(r1) == 0:
                continue
            for mapping in self._mappings:
                d1: int = mapping['delta']
                r2: range = range(mapping['begin'], mapping['end'])
                # r3 is the intersected range
                r3: range = range(
                    max(r1[0], r2[0]),
                    min(r1[-1], r2[-1]) + 1
                )
                if len(r3):
                    # now subtract the intersected range from the original
                    if r1[-1] == r3[-1]:
                        r1 = range(r1[0], r1[-1] + 1 - len(r3))
                    else:
                        r1 = range(r1[0] + len(r3), r1[-1])

                    # shift r3
                    r3 = range(r3[0] + d1, r3[-1] + d1)
                    mapping_ranges.append(r3)
                if len(r1) == 0:
                    break
            if len(r1):
                mapping_ranges.append(r1)
                print(f"{self.name} appending r1 {r1}")
        return mapping_ranges

    def get_mapped_location_ranges(self, r1s: List[range]) -> List[range]:
        mapped_ranges: List[range] = self._find_mapping_ranges(r1s)
        if self.destination:
            mapped_ranges = self.destination.get_mapped_location_ranges(mapped_ranges)
        print(f"{self.name} has ranges {mapped_ranges}")
        return mapped_ranges


def get_seeds_and_linked_list(input_list) -> Tuple[List, Source]:
    seeds: List[int] = []
    head_source: Optional[Source] = None
    previous_source: Optional[Source] = None
    current_source: Optional[Source] = None
    for line in input_list:
        # first get the seeds and move on
        if line.startswith("seeds:"):
            _, seeds_str = line.split(': ')
            seeds = seeds_str.split()
            continue
        if len(line) == 0:
            continue
        if line.find(':') != -1:
            map_info, _ = line.split()
            source, dest = map_info.split("-to-")
            # special case, first time through
            if not previous_source:
                current_source = Source(source)
                head_source = current_source
            else:
                current_source = previous_source.destination
            next_source = Source(dest)
            current_source.destination = next_source
            previous_source = current_source
        if line[0].isdigit():
            dest_value, source_value, length = line.split()
            delta = int(dest_value) - int(source_value)
            current_source.add_range_map(
                source_begin=int(source_value),
                source_len=int(length),
                dest_delta=delta
            )

    return seeds, head_source


def part1(input_list) -> int:
    seeds, head_source = get_seeds_and_linked_list(input_list)
    min_seed_location: int = sys.maxsize
    for seed_location in seeds:
        min_seed_location = min(
            min_seed_location,
            head_source.get_mapped_location(int(seed_location))
        )
    return min_seed_location


def part2(input_list) -> int:
    seeds, head_source = get_seeds_and_linked_list(input_list)
    min_seed_location: int = sys.maxsize
    seed_ranges: List = []
    range_start: int = -1
    for seed in seeds:
        if range_start == -1:
            range_start = int(seed)
        else:
            seed_ranges.append(range(range_start, range_start + int(seed)))
            range_start = -1

    print('')
    new_seed_ranges = head_source.get_mapped_location_ranges(seed_ranges)
    print(new_seed_ranges)
    min_seed_location: int = sys.maxsize
    for seed_range in new_seed_ranges:
        min_seed_location = min(min_seed_location, seed_range[0])
    print(min_seed_location)
    return min_seed_location
