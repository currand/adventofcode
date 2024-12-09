import os
import re
import asyncio
from icecream import ic
from collections import OrderedDict
import aiofiles

TEST = False

filedir = os.path.dirname(__file__)
day = filedir[-2:]
if TEST:
    infile = filedir + f'/test{day}.txt'
else:
    infile = filedir + f'/day{day}.txt'

def parse_almanac(infile):
    with open(infile, 'r') as f:
        input_data = f.read().strip()
    sections = input_data.split('\n\n')
    seeds = list(map(int, sections[0].split(': ')[1].split()))
    seed_ranges = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
    
    maps = []
    for section in sections[1:]:
        map_lines = section.split('\n')[1:]
        current_map = []
        for line in map_lines:
            dest_start, src_start, range_length = map(int, line.split())
            current_map.append((dest_start, src_start, range_length))
        maps.append(current_map)
    
    return seed_ranges, maps

def transform_ranges(ranges, current_map):
    new_ranges = []
    while ranges:
        start, length = ranges.pop(0)
        for dest_start, src_start, map_length in current_map:
            overlap_start = max(start, src_start)
            overlap_end = min(start + length, src_start + map_length)
            
            if overlap_start < overlap_end:
                # Transformed range
                new_start = dest_start + (overlap_start - src_start)
                new_length = overlap_end - overlap_start
                new_ranges.append((new_start, new_length))
                
                # Remaining ranges to process
                if overlap_start > start:
                    ranges.append((start, overlap_start - start))
                if start + length > overlap_end:
                    ranges.append((overlap_end, start + length - overlap_end))
                break
        else:
            # No mapping found, keep original range
            new_ranges.append((start, length))
    
    return new_ranges

def solve_part2(input_data):
    seed_ranges, maps = parse_almanac(input_data)
    
    for current_map in maps:
        seed_ranges = transform_ranges(seed_ranges, current_map)
    
    return min(start for start, _ in seed_ranges)

print(solve_part2(infile))
