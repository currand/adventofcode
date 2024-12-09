import os
import re
from icecream import ic
from collections import OrderedDict

TEST = False

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

def process_seed(seed, seed_map):
    current_mapping = seed
    for k in seed_map.keys():
        for map in seed_map[k]['map']:
            offset = map[0][0] - map[1][0]
            if current_mapping in range(map[0][0], map[0][1] + 1):
                current_mapping = current_mapping - offset
                break
    return current_mapping

if __name__ == '__main__':
    mappings = []
    seeds, seed_map = parse_input(lines)
    for seed in seeds:
        mappings.append(process_seed(seed, seed_map))
        ic("Finished a seed")
    
    ic(min(mappings))
