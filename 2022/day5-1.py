import re

def get_input(filename, no_strip=True):
    with open(filename, 'r') as fh:
        return fh.readlines()

lines = get_input('day5.txt')
stacks = []
for i,line in enumerate(lines):
    if not line.startswith(' 1'):
        stacks.append([line[i:i+3] for i in range(0, len(line), 4)])
    else:
        break

columns = []
stacks = list(map(list, zip(*stacks)))
for stack in stacks:
    column = []
    for item in stack:
        if item != '   ':
            column.append(item)
    columns.append(column)

moves = []
for line in lines[i+2:]:
    matches = re.match(r'move (\d+) from (\d+) to (\d+)', line)
    moves.append((int(matches.group(1)), int(matches.group(2)), int(matches.group(3))))

for move in moves:
    to_move = columns[move[1]-1][:move[0]][::-1]
    del columns[move[1]-1][:move[0]]
    columns[move[2]-1] = to_move + columns[move[2]-1]

out = [x[0] for x in columns]
out = ''.join(out).replace('[','').replace(']', '')

print(out)
