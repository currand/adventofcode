import os
import re
from collections import OrderedDict

TEST = True

filedir = os.path.dirname(__file__)
day = filedir[-2:]
if TEST:
    infile = filedir + f'/test{day}.txt'
else:
    infile = filedir + f'/day{day}.txt'

lines = [x.strip() for x in open(infile, 'r')]

REGEX_TITLE = re.compile(r'^(\w+)-to-(\w+)\smap:$')
REGEX_MAP = re.compile(r'^(\d+)\s(\d+)\s(\d+)$')

def parse_input(lines):
    seed_map = OrderedDict()
    for line in lines:
        if line.startswith('seeds'):
            seeds = [int(x) for x in line.strip('seeds: ').split()]
        elif len(match:= re.split(REGEX_TITLE, line)) > 1:
            title = match[1] + '-to-' + match[2]
            seed_map[title] = {
                'source': match[2],
                'dest': match[1],
                'map': []
            }
        elif len(match:= re.split(REGEX_MAP, line)) > 1:
            nums = [int(x) for x in match if x != '']
            source_range = (nums[1], nums[1] + nums[2] - 1)
            dest_range = (nums[0], nums[0] + nums[2] - 1)
            seed_map[title]['map'].append([source_range, dest_range])
    
    return seeds, seed_map

def map_seed(seed, map):

    if seed < map[0][0]:
        return seed
    elif __is_between(seed, map[0]):
        return seed + map[1][0] - map[0][0]
    else:
        return seed

def process_seed(seed, seed_map):
    current_mapping = seed
    for k in seed_map.keys():
        for map in seed_map[k]['map']:
            current_mapping = map_seed(current_mapping, map)
    
    return current_mapping

def __is_between(num: int, num_range: tuple) -> bool:
    return num >= num_range[0] and num <= num_range[1]

if __name__ == '__main__':
    seeds, seed_map = parse_input(lines)
    for seed in seeds:
        print(process_seed(seeds[1], seed_map))
    pass
