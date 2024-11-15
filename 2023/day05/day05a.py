import os
import re

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
    seed_map = {}
    for line in lines:
        if line.startswith('seeds'):
            seed_map['seeds'] = [int(x) for x in line.strip('seeds: ').split()]
        elif len(match:= re.split(REGEX_TITLE, line)) > 1:
            title = match[1] + '-' + match[2]
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
    
    return seed_map

def map_seed(map, num):
    output = []
    if is_between(num, map[0]):
        offset = map[1][0] - map[0][0]
        return num + offset
    elif num < 



def is_between(num, num_range):
    return num >= num_range[0] and num <= num_range[1]

if __name__ == '__main__':
    seed_map = parse_input(lines)
    out = map_seed(seed_map['seed-soil']['map'][1], 50)
    pass
