import os

TEST = False

filedir = os.path.dirname(__file__)
day = filedir[-2:]
if TEST:
    infile = filedir + f'/test{day}.txt'
else:
    infile = filedir + f'/day{day}.txt'

with open(infile, 'r') as f:
    lines = [line.strip() for line in f]

def parse_card(card: str) -> dict:
    output = {}
    name, numbers = card.split(':')
    winners, nums_have = numbers.split(' | ')
    output['name'] = name.replace('Game ', '')
    output['winners'] = {int(x) for x in winners.split()}
    output['nums_have'] = {int(x) for x in nums_have.split()}
    output['intersect'] = output['winners'].intersection(output['nums_have'])

    return output

final = []
for line in lines:
    card = parse_card(line)
    if len(card['intersect']) > 0:
        # print(2**(len(card['intersect'])-1))
        final.append(2**(len(card['intersect'])-1))
    else:
        final.append(0)

print(sum(final))
