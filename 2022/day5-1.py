import re

def get_input(filename):
    with open(filename, 'r') as fh:
        return fh.readlines()

lines = get_input('test5.txt')
stacks = []
for i,line in enumerate(lines):
    if not line.startswith(' 1'):
        stacks.append([line[i:i+3] for i in range(0, len(line), 4)])
    else:
        break

stacks = list(map(list, zip(*stacks)))
# need to get rid of '   ' at top of lists


moves = []
for line in lines[i+2:]:
    matches = re.match(r'move (\d+) from (\d+) to (\d+)', line)
    moves.append((int(matches.group(1)), int(matches.group(2)), int(matches.group(3))))

for move in moves:
    to_move = stacks[move[1]][:move[0]]
    pass


pass
