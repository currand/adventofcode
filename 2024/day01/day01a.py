import os
from functools import reduce

TEST = False

filedir = os.path.dirname(__file__)
day = filedir[-2:]
if TEST:
    infile = filedir + f'/test{day}.txt'
else:
    infile = filedir + f'/day{day}.txt'

lines = [x.strip() for x in open(infile, 'r')]

def parse_lines(lines):
    l1 = []
    l2 = []
    i = 0
    for line in lines:
        a,b = map(int, line.split())
        l1.append(a)
        l2.append(b)
    return zip(sorted(l1),sorted(l2))


if __name__ == '__main__':
    out = parse_lines(lines)
    t = reduce(lambda a,b: a+b, [max(x) - min(x) for x in out])
    print(f'Answer: {t}')